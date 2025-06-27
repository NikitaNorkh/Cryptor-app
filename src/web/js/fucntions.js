// Animation when page changes
// <!-- Анимации при переходе -->
$(document).ready(function() {
	$('a').on('click', function(event) {
		event.preventDefault();
		 
		var nextPage = $(this).attr('href');
		 
	$('body').fadeOut(500, function() {
		window.location.href = nextPage;
	});
	});
});