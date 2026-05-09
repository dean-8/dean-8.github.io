// auto update copyright year
document.getElementById('year').textContent = new Date().getFullYear(); 

function dropdown_menu(id){
  let aa = document.getElementById(id);
  if (aa.style.display === "none" || aa.style.display === ""){
    aa.style.display = "block";
  }
  else{
    aa.style.display = "none";
  }
  return false;
}