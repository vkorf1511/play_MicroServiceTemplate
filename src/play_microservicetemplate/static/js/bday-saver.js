const birthdayInput = document.querySelector("#birthday");
const status = document.querySelector("#status");
const savedBirthday = localStorage.getItem("birthday");

if (savedBirthday) 
    birthdayInput.value = savedBirthday;

document.querySelector("#birthday-form").addEventListener("submit", (event) => {
    event.preventDefault();
    localStorage.setItem("birthday", birthdayInput.value.trim());
    status.textContent = "Birthday saved.";
});