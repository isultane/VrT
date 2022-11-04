$(document).ready(function() {

	$('form').on('submit', function(event) {

		$.ajax({
			data : {
				name : $('#a').val()

			},
			type : 'POST',
			url : '/predict'
		})
		.done(function(data) {

				$('#output').text(data.output).show();



		});

		event.preventDefault();

	});

});