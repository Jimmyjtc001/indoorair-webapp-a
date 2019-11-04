function onDashboardClick() {
  const temperature = document.getElementById("temperature").value;
  console.log(temperature);
  const co2 = document.getElementById("co2").value;
  console.log(co2);
  const tvoc = document.getElementById("tvoc").value;
  console.log(tvoc);
  const humidity = document.getElementById("humidity").value;
  console.log(humidity);
  const pressure = document.getElementById("pressure").value;
  console.log(pressure);

  var xhttp = new XMLHttpRequest();
   xhttp.onreadystatechange = function() {
     if (this.readyState == 4 && this.status == 200) { // This is the callback function
         // Get the string data that the server sent us.
         if (this.readyState == 4 && this.status == 200) {
           data = JSON.parse(this.responseText);
           document.getElementById('temp_average').innerHTML =data.temp_average;
           document.getElementById('press_average').innerHTML = data.press_average;
           document.getElementById('co2_average').innerHTML = data.co2_average;
           document.getElementById('tvoc_average').innerHTML = data.tvoc_average;
           document.getElementById('humidity_average').innerHTML = data.humidity_avg;
         }
       }
     }
       xhttp.open('POST', "{% url 'dashboard_api' %}", true);
       xhttp.setRequestHeader("content-type", "application/x-www-form-urlencoded");
       xhttp.send("&temp_average="+temperature+"&press_average="+pressure+"&co2_average="+co2+"&tvoc_average="+tvoc+"&humidity_average="+humidity);

}
