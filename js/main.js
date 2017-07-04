$(document).ready(function(){
    //localization
    geoip2.city(function (location) {
        var locString = location.city.names.ru +
            ", " + location.subdivisions[0].names.ru;
        $(".geo").first().text("Регион: " + locString);
        $.notify(
            {
                icon: 'glyphicon glyphicon-globe',
                title: locString,
                message: 'Верно?'
            },
            {
                type: 'info',
                allow_dismis: true,
                placement: {
                    from: 'top',
                    align: 'left'
                },
                offset: {x: 20, y: 60},
                position: 'absolute',
                mouse_over: 'pause',
                delay: 5000,
                icon_type: 'string',
                template: '<div data-notify="container" class="col-xs-11 col-sm-3 alert alert-{0}" role="alert">' +
                '<button type="button" aria-hidden="true" class="close" data-notify="dismiss">×</button>' +

                '<span data-notify="title">Ваш регион: <b>{1}</b></span> ' +
                '<div class="text-center"><span data-notify="message">{2}</span></div>' +
                '<div class="text-center">' +
                '<a class="btn btn-info btn-sm" data-notify="dismiss">ДА</a>' +
                '<span>&nbsp;</span>' +
                '<a class="btn btn-info btn-sm" data-notify="dismiss" id="button_error_region">НЕТ</a>' +
                '</div>' +
                '</div>'
            }
        )


    });
    //language=JQuery-CSS
    $('.reviews-carousel').slick({
        arrows: true,
        slidesToShow: 1,
        autoplay: true,
        autoplaySpeed: 2000
    });

});


