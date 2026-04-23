function myFunction(){
	const colours = ["red","blue","green","yellow","orange","purple","pink","brown","black","white","gray","cyan","magenta","lime","teal","indigo","violet","gold","silver","beige","coral","crimson","navy","turquoise","lavender","salmon","plum","orchid","chocolate","tan","khaki","azure","mintcream","ivory","maroon","olive","aqua","fuchsia","darkblue","darkgreen","darkred","darkorange","darkviolet","deeppink","dodgerblue","firebrick","forestgreen","hotpink","lightblue","lightgreen","lightcoral","lightsalmon","mediumblue","mediumseagreen","mediumslateblue","midnightblue","palegreen","peachpuff","peru","powderblue","rosybrown","royalblue","seagreen","skyblue","slateblue","springgreen","steelblue","tomato","wheat","yellowgreen"]

	var colour1 = colours[Math.floor(Math.random()*colours.length)];
	var colour2 = colours[Math.floor(Math.random()*colours.length)];
	document.body.style.backgroundImage = "linear-gradient(to bottom right, " + colour1 + " , " + colour2 + ")";
}



function dropdownspec(){    //this is when the spec button is pressed, the image and <a> tag update
	
	document.getElementById("img-links").href = "https://qualifications.pearson.com/content/dam/pdf/A%20Level/Mathematics/2017/specification-and-sample-assesment/a-level-l3-mathematics-specification-issue4.pdf";
	document.getElementById("spec-dropdown").src =  "https://pdacademy.pearson.com/content/dam/one-dot-com/one-dot-com/pd-academy/products/Alevel-Maths.jpg" ;
	
}

function dropdownresources(){   //this is when the resources button is pressed, the image and <a> tag update
	document.getElementById("img-links").href = "https://www.physicsandmathstutor.com/maths-revision/a-level-edexcel/";
	document.getElementById("spec-dropdown").src =  "pmt_img.png" ;
}

function validateForm(){
	let a = true
	let fname = document.forms["myForm"]["fname"].value;
	let lname = document.forms["myForm"]["lname"].value;
	const users = [fname,lname]; 
	// In a real application, this data would be stored in a SQL database.
	// e.g INSERT INTO users (fname, lname) VALUES ('John', 'Doe');
	// This inserts the first and last name entered in the form into the users table.	


	if (fname==""){ 			//checks if first name is empty
	document.getElementById("error_msg").innerHTML = "ENTER FIRST NAME!!!!";
	a = false;
	}
	else if (lname==""){ 			//checks if last name is empty
	document.getElementById("error_msg").innerHTML = "ENTER LAST NAME!!!!";
	a = false;
	}
	
	else {
	document.getElementById("home_button").href = "website.html";
	document.getElementById("home_button").innerHTML = "please click me";
	}
	

	if (a==false){		// creates the error message box as its "invisible before this"
	document.getElementById("error_msg").style.display = "false";
	document.getElementById("error_msg").style.background = "black";
	document.getElementById("error_msg").style.border = "6px solid grey";
	document.getElementById("error_msg").style.borderColor = "grey";
	document.getElementById("error_msg").style.borderRadius = "3px";
	document.getElementById("error_msg").style.color = "red";
	}	

	else {			// removes the error if form is correct
	document.getElementById("error_msg").style = "none";
	document.getElementById("error_msg").innerHTML = "";
	document.getElementById("error_msg").style.background = "none";


	}

	return false;
}


function scaleFunc() {   //outputs value of the scale on the form
	let scaleValue = document.getElementById("myScale").value;
	document.getElementById("output_num").innerHTML = scaleValue;
	return false;
}




function csspec(){   //this is when the spec button is pressed, the image and <a> tag update
	
	document.getElementById("img-links").href = "https://www.ocr.org.uk/images/170844-specification-accredited-a-level-gce-computer-science-h446.pdf";
	document.getElementById("spec-dropdown").src =  "https://miro.medium.com/v2/1*0Giup3EYsyyG4EmYPjh37g.png" ;
	
}

function csresources(){      //this is when the resources button is pressed, the image and <a> tag update

	document.getElementById("img-links").href = "https://www.physicsandmathstutor.com/computer-science-revision/a-level-ocr/";
	document.getElementById("spec-dropdown").src =  "cspmt.png" ;
}

function physspec(){  //this is when the spec button is pressed, the image and <a> tag update
	
	document.getElementById("img-links").href = "https://cdn.sanity.io/files/p28bar15/green/c84fb691cf808ff97ba17ffce6f458f837016dc9.pdf";
	document.getElementById("spec-dropdown").src =  "phys-spec.png" ;
	
}

function physresources(){    //this is when the resources button is pressed, the image and <a> tag update
	document.getElementById("img-links").href = 
"https://www.physicsandmathstutor.com/physics-revision/a-level-aqa/";
	document.getElementById("spec-dropdown").src =  "physpmt.png" ;
}
