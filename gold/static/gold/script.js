var gold = document.getElementById("gold");
var button = document.getElementById("button");
var main = document.getElementById("main");
var price = 0;
var key = "8p7rzN6cpTCFvXXqTwLp";
var message = null;
var unit = document.getElementById("unit");

fetch("https://www.quandl.com/api/v3/datasets/LBMA/GOLD?limit=1&api_key="+ key).then(response => response.json()).then(json => {price = json.dataset.data[0][2]; gold.textContent = "The Price of Gold is $" + price + " per troy ounce";});


 
button.onclick = function() {
	var num = Number(document.getElementById("num").value);
	if (isNaN(num) || price === 0){ 
		message = document.createElement("div"); 
		message.setAttribute("class", "red shadowed stuff-box");
		message.textContent = "Something went wrong";
		message.onclick = function() {this.remove();};
		document.querySelector("body").insertBefore(message, main.nextSibling);
	}
	else{
		var next = document.createElement("div");
		next.setAttribute("class", "green shadowed stuff-box");
		fetch("../unitconv/?value=" + num + "&start=" + unit.value + "&end=troy ounces").then(response => response.json()).then(json => next.textContent = "You are worth $" + json.conversion * price).then(noting => {next.onclick = function() {this.remove();};}).then(document.querySelector("body").insertBefore(next, main.nextSibling));
	}
}
