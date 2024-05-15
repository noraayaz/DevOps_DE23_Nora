// Functions that will run when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', function() {
    updateCurrentDate();
    loadTableData();
});

// Function to update the date and time information in the header
function updateCurrentDate() {
    const currentDateElement = document.getElementById('currentDate');
    const now = new Date();
    const dateString = now.toISOString().slice(0, 10); // Date in YYYY-MM-DD format
    const timeString = now.toTimeString().slice(0, 5); // Time in HH:MM format
    currentDateElement.textContent = `${dateString} ${timeString} The current cool customers`;
}

// Function to load data and update the table
function loadTableData() {
    const allMoviesTBody = document.querySelector("#allItems tbody");
    fetch('./data.json')
        .then((response) => response.json())
        .then((json) => {
            showTable(json);
        });

    function showTable(moviesArray) {
        allMoviesTBody.innerHTML = "";
        for (let i = 0; i < moviesArray.length; i++) {
            let trText = `<tr><th scope="row">${moviesArray[i].Givenname} ${moviesArray[i].Surname}</th><td>${moviesArray[i].Country}</td><td>${moviesArray[i].Birthday.substring(0,4)}</td></tr>`;
            allMoviesTBody.innerHTML += trText;
        }
    }
}
