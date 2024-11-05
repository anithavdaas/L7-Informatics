function addFlavor() {
    const flavorName = document.getElementById('flavorName').value;
    const season = document.getElementById('season').value;

    fetch('/add_flavor', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ flavor_name: flavorName, season: season })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);  // Notify user of successful addition
    })
    .catch(error => console.error('Error:', error));
}

function fetchFlavors() {
    fetch('/flavors')
        .then(response => response.json())
        .then(data => {
            const flavorList = document.getElementById('flavorList');
            flavorList.innerHTML = ''; // Clear list before populating

            data.forEach(flavor => {
                const li = document.createElement('li');
                li.textContent = `${flavor[1]} - Available in ${flavor[2]}`;
                flavorList.appendChild(li);
            });
        })
        .catch(error => console.error('Error:', error));
}
