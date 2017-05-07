var map;
var infoWindow;
var service;

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: {
            lat: -33.867,
            lng: 151.206
        },
        zoom: 17,
        mapTypeId: 'roadmap'
    });

    infoWindow = new google.maps.InfoWindow();
    service = new google.maps.places.PlacesService(map);
    var input = document.getElementById('pac-input');
    var searchBox = new google.maps.places.SearchBox(input);
    map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);
    var markers = [];
    map.addListener('bounds_changed', function() {
        searchBox.setBounds(map.getBounds());
    });
    searchBox.addListener('places_changed', function() {
        var places = searchBox.getPlaces();

        if (places.length == 0) {
            return;
        }

        // Clear out the old markers.
        markers.forEach(function(marker) {
            marker.setMap(null);
        });
        markers = [];

        // For each place, get the icon, name and location.
        var bounds = new google.maps.LatLngBounds();

        //map.addListener('idle', performSearch);
        places.forEach(function(place) {
            if (!place.geometry) {
                console.log("Returned place contains no geometry");
                return;
            }
            var icon = {
                url: place.icon,
                size: new google.maps.Size(71, 71),
                origin: new google.maps.Point(0, 0),
                anchor: new google.maps.Point(17, 34),
                scaledSize: new google.maps.Size(25, 25)
            };

            // Create a marker for each place.
            markers.push(new google.maps.Marker({
                map: map,
                icon: icon,
                title: place.name,
                position: place.geometry.location
            }));

            if (place.geometry.viewport) {
                // Only geocodes have viewport.
                bounds.union(place.geometry.viewport);
            } else {
                bounds.extend(place.geometry.location);
            }
        });
        map.fitBounds(bounds);
    });

    // The idle event is a debounced event, so we can query & listen without
    // throwing too many requests at the server.
    map.addListener('bounds_changed', radarSearch);
    document.getElementById('parkButton').addEventListener('click', function() {
        postParking(service,map,infoWindow);
    });

}

function radarSearch() {
    var request = {
        //bounds: map.getBounds(),
        location: map.getCenter(),
        radius: 200,
        type: ['parking'],
    };
    service.radarSearch(request, callback);
}


function callback(results, status) {
    if (status !== google.maps.places.PlacesServiceStatus.OK) {
        console.error(status);
        return;
    }
    for (var i = 0, result; result = results[i]; i++) {
        if (result.name != "Bike Rack") {
            addMarker1(result);
        }


    }
}

function addMarker1(place) {
    var tmpName = place.name;
    if (tmpName !== "Bike Rack") {
        var marker = new google.maps.Marker({
            map: map,
            position: place.geometry.location,

        })
    };

    google.maps.event.addListener(marker, 'click', function() {
        service.getDetails(place, function(result, status) {
            if (status !== google.maps.places.PlacesServiceStatus.OK) {
                console.error(status);
                return;
            }

            var placeAddNum = result.address_components[0].long_name;
            var placeAddStr = result.address_components[1].long_name;
            var placeAddSubb = result.address_components[2].long_name;
            var placeAddCountry = result.address_components[4].long_name;
            var placeAddress = placeAddNum.concat(" ", placeAddStr, ", ", placeAddSubb, ", ", placeAddCountry);
            var placeID = result.place_id;
            var placeName = result.name;
            //var placeDets = '<p>' + result.formatted_address + '</p>' + '<p>' + placeName + '</p>' + '<p id="place_ID"> ID : ' + '</p>' + '<input id="parkButton" type="button" value="Park here">';
            var placeDets = '<p>' + result.formatted_address + '</p>' + '<p>' + placeName + '</p>' + '<p id="place_ID"> ID : '+placeID + '</p>' + '<form method ="post"><buttton data-place-name="'+ placeName +'" data-place-id="'+ placeID +'" onClick="postParkID(this)">Park here</button></form>';

            infoWindow.setContent(placeDets);
            infoWindow.open(map, marker);
        });
    });
}
function postParkID(e){
    window.alert(e.getAttribute("data-place-id"));
}
function postPark(e) {
    $.ajax({}); 
}
