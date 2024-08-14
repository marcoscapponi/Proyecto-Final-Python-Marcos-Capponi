/*!
* Start Bootstrap - Landing Page v6.0.6 (https://startbootstrap.com/theme/landing-page)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-landing-page/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

function updateDate() {
    const dateElement = document.getElementById('current-date');
    const now = new Date();
    const options = {year: 'numeric', month: 'long', day: 'numeric'};
    const formattedDate = now.toLocaleDateString('es-Es', options);
    dateElement.textContent = formattedDate
}
window.onload = updateDate;

setInterval(updateDate, 86400000)