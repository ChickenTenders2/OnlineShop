$(document).ready(function() {
    $('#payment-form').submit(function(e) {
        var cardNumber = $('#card-number').val();
        var cardNumberWithoutSpaces = cardNumber.replace(/ /g, '');
        var cardNumberWithoutDashes = cardNumberWithoutSpaces.replace(/-/g, '');

        if (cardNumberWithoutDashes.length != 16 || isNaN(cardNumberWithoutDashes)) {
            alert('Please enter a valid 16-digit card number (spaces and dashes are allowed).');
            e.preventDefault();
        }

        var cvv = $('#cvv').val();
        if (cvv.length < 3 || cvv.length > 4 || isNaN(cvv)) {
            alert('Please enter a valid CVV (3 or 4 digits).');
            e.preventDefault();
        }

        var cardholderName = $('#cardholder-name').val();
        if (cardholderName.trim() === '') {
            alert('Please enter the cardholder name.');
            e.preventDefault();
        }

        var address = $('#address').val();
        if (address.trim() === '') {
            alert('Please enter your address.');
            e.preventDefault();
        }
    });
});