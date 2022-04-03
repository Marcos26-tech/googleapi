function initMap(data) {
    
    var center = {lat: data[0][`latitude`], data[0][`longitude`]};
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 4,
        center: center
    });
    
    var infowindow =  new google.maps.InfoWindow({});
    var marker;
    
    data.forEach(e => {
        marker = new google.maps.Marker({
        position: new google.maps.LatLng(e[`latitude`], e[`longitude`]),
        map: map,
        title: e[`address`],
    });
        google.maps.event.addListener(marker, 'click', (function (marker) {
            return function () {
                infowindow.setContent(`State: ${e[`state`]<br>County: ${e[`location`]}<br>Address: ${e[`address`]}`);
                infowindow.open(map, marker);
            }
        })(marker));
    });
}