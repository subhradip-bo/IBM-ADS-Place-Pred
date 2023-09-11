
document.addEventListener("DOMContentLoaded", function () {
    
    var predElement = document.getElementById("pred");

    var initialYValue = predElement.textContent.trim();

    if (initialYValue === "High chances of getting Placed" || initialYValue === "Low chances of getting Placed") {
        
        console.log("Value of {{y}}:", initialYValue);
        if (initialYValue === "High chances of getting Placed") {
            predElement.style.color = "green";
        } else {
            predElement.style.color = "red";
        }
        predElement.classList.add("fade-in");

    }


    const slideButton = document.getElementById("submit");
var myInput1 = document.querySelector('#ag');
var myInput2 = document.querySelector('#ge');
var myInput3 = document.querySelector('#st');
var myInput4 = document.querySelector('#in');
var myInput5 = document.querySelector('#cg');
var myInput6 = document.querySelector('#ba');

slideButton.addEventListener("click", function(e) {
    if(myInput1.value.trim() === '' || myInput2.value.trim() === '' || myInput3.value.trim() === '' ||
     myInput4.value.trim() === '' || myInput5.value.trim() === '' || myInput6.value.trim() === '') {
        e.preventDefault(); 
        alert('Please fill all the fields before submitting');
    }
});


});