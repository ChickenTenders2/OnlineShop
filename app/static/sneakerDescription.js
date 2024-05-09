document.querySelectorAll('.product-list li').forEach(function(li) {
    li.addEventListener('mouseover', function() {
        console.log("Mouse is over the image"); 
        var sneakerId = this.getAttribute('data-id');
        fetch('/sneaker-description/' + sneakerId)
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    console.error(data.error);
                } else {
                    var descriptionDiv = this.querySelector('.description');
                    var truncatedDescription = data.description.length > 100 ? data.description.substring(0, 100) + '... (Click image to read more)' : data.description;
                    descriptionDiv.textContent = truncatedDescription;
                    descriptionDiv.style.display = 'block';
                }
            });
    });

    li.addEventListener('mouseout', function() {
        console.log("Mouse left the image"); 
        var descriptionDiv = this.querySelector('.description');
        descriptionDiv.style.display = 'none';
    });
});