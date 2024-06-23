document.addEventListener('DOMContentLoaded', function () {
    var links = document.querySelectorAll('.nav-link');
    links.forEach(function(link) {
        link.addEventListener('click', function() {
            links.forEach(function(link) {
                link.parentElement.classList.remove('active');
            });
            this.parentElement.classList.add('active');
        });
    });
});


