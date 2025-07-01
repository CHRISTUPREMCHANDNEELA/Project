const users = [
    {
        username: "prem1996",
        password: "Raju2000",
        Name: "premchand",
        accountNumber: "SWB624137",
        BALANCE: 5000
    },
    {
        username: "Kiran2905",
        password: "Kiran@2014",
        Name: "Kiran Kumar",
        accountNumber: "SWB501005",
        balance: 6267
    }
];
document.getElementById("loginform").addEventListener("submit",function (e) )
{
    e.preventDefault();
    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value.trim();
    const error message = document.getElementById("error message");
    const user = users.find(u=>u.username === username && u.password === password);
    if (user)
    {
        sessionStorage.setItem("loggeduser",);
        window.location.href = "dashboard.html";   
    }
    else
    {
        error message.textContent = "invalid username or password.";
    }
}