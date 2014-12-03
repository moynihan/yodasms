/*
$(document).ready(function () {
    $("#translate-btn").on('click', function () {

        $.ajax({
            url: 'https://yoda.p.mashape.com/yoda',
            type: 'GET',
            data: {sentence: $("#boxArea").val()},
            datatype: 'json',
            success: function (data) {
                $("#yoda-message").text(data)
            },
            error: function (err) {
                alert('error');
            },
            beforeSend: function (xhr) {
                xhr.setRequestHeader("X-Mashape-Authorization", "Mn172XYNOMmshy9qqxv2Ge3fo0Hqp1U2bNtjsnoQHQTDBfCJ6s");
            }
        });
    });
});
*/