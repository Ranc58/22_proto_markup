import staticjinja as sj


USER = 'Иван Федорович Крузенштерн'


index_content = {
    'user': USER,
    'reviews': 4,
    'author': 'Иван Федорович Крузенштерн, г. Улан-Удэ',
    'review_text': 'Лучшего товара я просто не видел! Потрясающе!!'
                   'Буду брать тут всегда! Абсолютно все! Perfect!!',
    'requests': 4,
    'time': 'вчера, в 12:50',
    'request_info': '60шт. ПК от 72-15  до ПК 21-15,'
                    'Криводановка, с доставкой.',
    'request_person_name': 'Алексей',
    'views_value': '12 просмотров',
    'footer': True
}

org_catalog_content = {
    'user': USER,
    'tables': 4,
    'company_name': 'ООО Строй-Сервис-Монтаж',
    'company_location': 'Новосибирск',
    'company_production': 'ЖБИ, бетон',
    'company_address': 'Под часами, на том же месте',
    'company_phone_number': '00-00-00',
    'footer': True
}

organisation_content = {
    'user': USER,
    'specification': 'ЖБИ',
    'company_name': 'ООО Строй-Сервис-Монтаж',
    'company_location': 'Новосибирск',
    'company_production': 'ЖБИ, бетон',
    'company_address': 'Под часами, на том же месте',
    'company_phone_number': '00-00-00',
    'specialties':  ['Плиты', 'Перекрытия', 'Доставляем быстро'],
    'footer': True
}

requests_content = {
    'user': USER,
    'requests': 6,
    'time': 'вчера, в 12:50',
    'request_info': '60шт. ПК от 72-15  до ПК 21-15,'
                    'Криводановка, с доставкой.',
    'request_person_name': 'Алексей',
    'views_value': '12 просмотров',
    'footer': True
}

specification_content = {
    'user': USER,
    'specification': 'ЖБИ',
    'tables': 4,
    'company_name': 'ООО Строй-Сервис-Монтаж',
    'company_location': 'Новосибирск',
    'company_production': 'ЖБИ, бетон',
    'company_address': 'Под часами, на том же месте',
    'company_phone_number': '00-00-00',
    'footer': True
}

profile_content = {
    'user': USER,
    'footer': False
}


if __name__ == "__main__":
    site = sj.make_site(outpath='static', contexts=[
        ('index.html', index_content),
        ('org_catalog.html', org_catalog_content),
        ('organisation.html', organisation_content),
        ('profile.html', profile_content),
        ('requests.html', requests_content),
        ('specification_catalog.html', specification_content)
    ])
    site.render()
