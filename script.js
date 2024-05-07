let usernameMessage = document.querySelector('.username-validation')
let passwordMessage = document.querySelector('.password-validation')

let usernameInput = document.querySelector('.username')
let passwordInput = document.querySelector('.password')

function usernameValidation () {
    if (usernameInput.value.length < 27) {
        usernameMessage.style.color = 'red'
        usernameMessage.innerHTML = 'باید شامل 27 نویسه باشد'
        usernameMessage.style.display = 'block'
    } else {
        usernameMessage.style.color = 'green'
        usernameMessage.innerHTML = '   ایمیل صحیح است'
    }
}

function passwordValidation () {
    if (passwordInput.value.length < 8) {
        passwordMessage.style.color = 'red'
        passwordMessage.innerHTML = 'باید دارای 8 کاراکتر باشد '
        passwordMessage.style.display = 'block'
    } else {
        passwordMessage.style.color = 'green'
        passwordMessage.innerHTML = ' کلمه عبور صحیح است'
    }
}