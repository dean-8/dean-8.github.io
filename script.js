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

function showTooltip(e) {
  const tooltip = document.getElementById('tooltip');
  
  // Display briefly to calculate offset width
  tooltip.style.display = 'block';
  
  // Offset 10px to the left of the cursor, plus the element's full width
  const offsetLeft = e.clientX - tooltip.offsetWidth - 10;
  
  tooltip.style.left = offsetLeft + 'px';
  tooltip.style.top = (e.clientY + 15) + 'px';
}

function hideTooltip() {
  const tooltip = document.getElementById('tooltip');
  tooltip.style.display = 'none';
}