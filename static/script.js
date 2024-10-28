document.addEventListener('DOMContentLoaded', function() {
    const cpuUsageElement = document.getElementById('cpu-usage');
    const memoryUsageElement = document.getElementById('memory-usage');
    const diskUsageElement = document.getElementById('disk-usage');
    const historicalBody = document.getElementById('historical-body');
    const refreshButton = document.getElementById('refresh-button');

    function fetchSystemStats() {
        fetch('/api/system-stats')
            .then(response => response.json())
            .then(data => {
                cpuUsageElement.textContent = data.cpu;
                memoryUsageElement.textContent = data.memory;
                diskUsageElement.textContent = data.disk;
                updateHistoricalData(data.cpu, data.memory, data.disk);
            })
            .catch(error => console.error('Error fetching system stats:', error));
    }

    function updateHistoricalData(cpu, memory, disk) {
        const newRow = document.createElement('tr');
        newRow.innerHTML = `<td>${cpu}</td><td>${memory}</td><td>${disk}</td>`;
        historicalBody.appendChild(newRow);
    }

    refreshButton.addEventListener('click', fetchSystemStats);
    
    // Fetch stats on page load
    fetchSystemStats();
});
