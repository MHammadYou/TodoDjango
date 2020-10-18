const form = document.getElementById('form')
const task = document.getElementById('task')
const errors = document.getElementById('errors')


form.addEventListener("submit", event => {
    errors.style.fontSize = "16px"
    if (task.value.length <= 0) {
        errors.innerText = "*Field Can't be empty"
        event.preventDefault()
    }
    if (task.value.length >= 100) {
        errors.innerText = "*Task Should be less than 100 characters long"
        event.preventDefault()
    }
})
