document.addEventListener('DOMContentLoaded', function () {
    const cpuCtx = document.getElementById('cpuChart').getContext('2d');
    const ramCtx = document.getElementById('ramChart').getContext('2d');
    const diskCtx = document.getElementById('diskChart').getContext('2d');
    const networkCtx = document.getElementById('networkChart').getContext('2d');

    new Chart(cpuCtx, {
        type: 'bar',
        data: {
            labels: cpuData.labels,
            datasets: [{
                label: 'CPU Usage (%)',
                data: cpuData.values,
                backgroundColor: '#FF6384'
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: { beginAtZero: true, max: 100 }
            }
        }
    });

    new Chart(ramCtx, {
        type: 'bar',
        data: {
            labels: ramData.labels,
            datasets: [{
                label: 'RAM Usage (MiB)',
                data: ramData.values,
                backgroundColor: '#36A2EB'
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: { beginAtZero: true }
            }
        }
    });

    new Chart(diskCtx, {
        type: 'bar',
        data: {
            labels: diskData.labels,
            datasets: [
                {
                    label: 'Reads (KiB/s)',
                    data: diskData.reads,
                    backgroundColor: '#FFCE56'
                },
                {
                    label: 'Writes (KiB/s)',
                    data: diskData.writes,
                    backgroundColor: '#4BC0C0'
                }
            ]
        },
        options: {
            responsive: true,
            scales: {
                y: { beginAtZero: true }
            }
        }
    });

    new Chart(networkCtx, {
        type: 'bar',
        data: {
            labels: networkData.labels,
            datasets: [{
                label: 'Network Usage (KiB/s)',
                data: networkData.values,
                backgroundColor: '#FFA726'
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: { beginAtZero: true }
            }
        }
    });
});

