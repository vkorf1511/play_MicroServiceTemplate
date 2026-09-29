const birthdayInput = document.querySelector("#birthday");
const status = document.querySelector("#status");
const savedBirthday = localStorage.getItem("birthday");
const submitButton = document.querySelector("#birthday-form button[type='submit']");
const loadLatestButton = document.querySelector("#load-latest");
const latestBirthdayInput = document.querySelector("#latest-birthday");

const today = new Date();
birthdayInput.max = [
    today.getFullYear(),
    String(today.getMonth() + 1).padStart(2, "0"),
    String(today.getDate()).padStart(2, "0")
].join("-");

if (savedBirthday) {
    const [day, month, year] = savedBirthday.split("/");
    birthdayInput.value = `${year}-${month}-${day}`;
}

document.querySelector("#birthday-form").addEventListener("submit", (event) => {
    event.preventDefault();
    const [year, month, day] = birthdayInput.value.split("-");
    const value = `${day}/${month}/${year}`;

    submitButton.disabled = true;
    status.textContent = "Saving birthday...";

    fetch("/api/birthdays", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ value })
    })
        .then(async (response) => {
            const result = await response.json();
            if (!response.ok) {
                throw new Error(result.detail || "Could not save birthday.");
            }
            localStorage.setItem("birthday", value);
            status.textContent = "Birthday saved.";
        })
        .catch((error) => {
            status.textContent = error.message;
        })
        .finally(() => {
            submitButton.disabled = false;
        });
});

loadLatestButton.addEventListener("click", async () => {
    loadLatestButton.disabled = true;
    status.textContent = "Loading latest birthday...";

    try {
        const response = await fetch("/api/birthdays/latest");
        const result = await response.json();
        if (!response.ok) {
            throw new Error(result.detail || "Could not load the latest birthday.");
        }
        latestBirthdayInput.value = result.value;
        status.textContent = "Latest birthday loaded.";
    } catch (error) {
        latestBirthdayInput.value = "";
        status.textContent = error.message;
    } finally {
        loadLatestButton.disabled = false;
    }
});