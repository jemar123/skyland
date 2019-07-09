// Messages
setTimeout(function(){
    $('#message').fadeOut('slow');
}, 3000);

// Inquiry
$('#inquiry_button').click(function(){

	$('#inquiry_modal').fadeIn('slow');

})
$('.close').click(function(){

	$('#inquiry_modal').fadeOut('slow');

})