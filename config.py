stopwords = ['как', 'куда', 'сегодня', 'я', 'он', 'она', 'они', 'лагать', 'работать', 'вчера', 'скоро', 'мало',
             'много', 'что', 'делать', 'какое', 'или', 'и', 'от', 'в', 'на', 'нас', 'вас', 'их', 'какими', 'это','то',
             'какой', 'почему', 'помогите', 'здравствуйте', 'всё', 'с', 'со', 'свой', 'мой','могут', 'ли', 'можно',
             'могут', 'может', 'для', 'при', 'за', 'по', 'но', 'к', 'но', 'проблема','такой', 'о', 'из',]


dictionary = {'https://spb.rt.ru/support/internet/connect/conduct-internet-in-house': {'интернет', 'дом', 'провести', 'квартира'},
    'https://spb.rt.ru/support/internet/connect/what-internet-speed-need': {'нужный', 'скорость', 'интернет', 'понять'},
    'https://spb.rt.ru/support/internet/connect/connection-technologies': {'технология', 'подключение', 'возможный', 'интернет'},
    'https://spb.rt.ru/support/internet/connect/tariffs-for-connecting-to-internet': {'действовать', 'подключение', 'тариф', 'интернет'},
    'https://spb.rt.ru/support/hometv/connect/documents-required-to-connect-internet': {'услуга', 'нужный', 'документ', 'подключение'},
    'https://spb.rt.ru/support/internet/connect/internet-connection-equipment': {'подключение', 'потребоваться', 'интернет', 'оборудование'},
    'https://spb.rt.ru/support/internet/connect/additional-features-of-home-internet': {'подключение', 'дополнительный', 'интернет', 'возможность'},
    'https://spb.rt.ru/support/phone/connect/find-current-tariff-plan-under-contract': {'тарифный', 'план', 'узнать', 'стоимость', 'текущий'},
    'https://spb.rt.ru/support/internet/tariff-service-management/speed-according-to-tariff-plan': {'узнать', 'тарифный', 'скорость', 'план'},
    'https://spb.rt.ru/support/internet/tariff-service-management/increase-internet-speed': {'увеличить', 'скорость', 'интернет'},
    'https://spb.rt.ru/support/hometv/control/change-tariff-plan': {'тарифный', 'изменить', 'план'},
    'https://spb.rt.ru/support/phone/control/temporarily-block-service': {'услуга', 'время', 'заблокировать'},
    'https://spb.rt.ru/support/internet/tariff-service-management/disable-service-without-contract-terminating': {'услуга', 'один', 'отключить'},
    'https://spb.rt.ru/support/hometv/control/relocation': {'перенести', 'адрес', 'другой', 'переезд', 'услуга'},
    'https://spb.rt.ru/support/phone/contract/contract-account-number': {'узнать', 'номер', 'счёт', 'лицевой'},
    'https://spb.rt.ru/support/phone/contract/combine-separate-account': {'счёт', 'объединить', 'разделить', 'лицевой'},
    'https://spb.rt.ru/support/phone/contract/renew-contract-another-person': {'переоформить', 'другой', 'договор', 'человек'},
    'https://spb.rt.ru/support/phone/contract/change-credentials-data': {'личность', 'дать', 'изменить', 'удостоверять', 'документ'},
    'https://spb.rt.ru/support/hometv/contract-management/change-my-contact-information': {'телефон', 'еmail', 'дать', 'контактный', 'изменить', 'номер'},
    'https://spb.rt.ru/legal': {'персональный', 'согласие', 'обработка', 'данные'},
    'https://spb.rt.ru/support/phone/contract/receive-notifications-or-advertisements': {'отказаться', 'реклама', 'уведомление'},
    'https://spb.rt.ru/support/hometv/contract-management/how-terminate-contract': {'отказаться', 'услуга', 'договор', 'расторгнуть'},
    'https://spb.rt.ru/support/internet/diagnostics/no-internet-access': {'нет', 'доступ', 'интернет'},
    'https://spb.rt.ru/support/internet/diagnostics/connection-breaks': {'соединение', 'разрыв'},
    'https://spb.rt.ru/support/internet/diagnostics/low-speed-internet': {'скорость', 'интернет', 'низкий'},
    'https://spb.rt.ru/support/internet/setting/everything-about-wifi-and-speed': {'нужно', 'wifi', 'знать', 'скорость'},
    'https://spb.rt.ru/support/phone/payment/contract-account-number': {'счёт', 'номер', 'узнать', 'договор', 'лицевой'},
    'https://spb.rt.ru/support/phone/payment/service-or-equipment-account-payment-methods': {'счёт', 'оплата', 'оборудование', 'выставление', 'порядок', 'услуга'},
    'https://spb.rt.ru/support/phone/payment/service-or-equipment-payment-amount': {'оплата', 'оборудование', 'узнать', 'услуга', 'сумма'},
    'https://spb.rt.ru/support/internet/payment/invoice-delivery-ways': {'счёт', 'получать', 'связь', 'услуга', 'способ'},
    'https://spb.rt.ru/support/phone/payment/available-payment-methods': {'счёт', 'оплатить'},
    'https://spb.rt.ru/support/internet/payment/find-out-if-payment-has-arrived': {'узнать', 'платёж', 'счёт', 'поступить'},
    'https://spb.rt.ru/support/internet/payment/payment-received-but-no-internet': {'платёж', 'интернет', 'поступить', 'нет', 'равно', 'если'},
    'https://spb.rt.ru/support/phone/payment/payment-has-not-been-received': {'счёт', 'платёж', 'поступить', 'не', 'если'},
    'https://spb.rt.ru/support/phone/payment/how-to-enable-auto-payment': {'автоплатёж', 'подключить'},
    'https://spb.rt.ru/support/phone/payment/how-return-balance-of-funds-using-non-cash-method': {'средство', 'вернуть', 'безналичный', 'денежный', 'остаток', 'способ'},
    'https://spb.rt.ru/support/phone/payment/how-transfer-payment-between-personal-accounts': {'счёт', 'перенести', 'платёж', 'между', 'лицевой'},
    'https://spb.rt.ru/support/phone/payment/how-to-activate-promised-payment': {'обещать', 'платёж', 'подключить'},
    'https://spb.rt.ru/support/documents#phone': {'договор', 'соглашение'},
    'https://spb.rt.ru/support/mobile/connect/become-client-rostelecom': {'клиент', 'стать', 'ростелеком'},
    'https://spb.rt.ru/support/mobile/connect/transition-rostelecom-with-your-number': {'переход', '«ростелеком»', 'номер'},
    'https://spb.rt.ru/support/mobile/payment/form-of-payment': {'оплата', 'форма'},
    'https://spb.rt.ru/support/mobile/payment/balance-and-payment': {'оплата', 'баланс'},
    'https://spb.rt.ru/mobile/mobile_tariff': {'тарифный', 'план'},
    'https://spb.rt.ru/support/mobile/control/services': {'услуга'},
    'https://spb.rt.ru/support/mobile/control/sim-card-and-phone-number': {'телефон', 'simкарта', 'номер'},
    'https://spb.rt.ru/support/mobile/control/order-of-dialing': {'набор', 'порядок', 'номер'},
    'https://spb.rt.ru/legal': {'персональный', 'обработка', 'данные'},
    'https://spb.rt.ru/support/phone/contract/terminate-contract': {'договор', 'расторгнуть'},
    'https://spb.rt.ru/bonus': {'бонус', 'программа'},
    'https://spb.rt.ru/support/mobile/setting/settings-mobile-internet': {'мобильный', 'интернет', 'настройка'},
    'https://spb.rt.ru/support/mobile/setting/settings-mobile-internet-roaming': {'мобильный', 'роуминг', 'интернет', 'настройка'},
    'https://spb.rt.ru/support/mobile/reference-information/self-service': {'самообслуживание'},
    'https://spb.rt.ru/support/documents#mobile': {'документ', 'справочник'},
    'https://spb.rt.ru/mobile/mobile_tariff#zone': {'зона', 'покрытие'},
    'https://spb.rt.ru/support/hometv/connect/connect-tv-to-house-apartment': {'квартира', 'подключить', 'тв', 'интерактивный', 'дом'},
    'https://spb.rt.ru/support/hometv/connect/what-is-interactive-tv': {'интерактивный', 'тв'},
    'https://spb.rt.ru/support/hometv/connect/interactive-tv-connection-technologies': {'возможный', 'технология', 'подключение', 'тв', 'интерактивный'},
    'https://spb.rt.ru/support/hometv/connect/tariffs-for-connecting-television': {'действовать', 'подключение', 'тв', 'интерактивный', 'тариф'},
    'https://spb.rt.ru/support/hometv/connect/television-connection-equipment': {'потребоваться', 'оборудование', 'подключение', 'тв', 'интерактивный'},
    'https://spb.rt.ru/support/hometv/connect/additional-features-of-home-television': {'дополнительный', 'подключение', 'тв', 'возможность', 'интерактивный'},
    'https://spb.rt.ru/support/hometv/control/interactive-tv-package-what-is-included': {'состав', 'пакет', 'входить', 'узнать', 'тв', 'интерактивный'},
    'https://spb.rt.ru/support/hometv/control/multiscreen': {'wink', '«мультискрин»', 'настроить'},
    'https://spb.rt.ru/support/hometv/control/disable-service': {'дополнительный', 'подключить', 'отключить', 'опция', 'тв', 'интерактивный'},
    'https://spb.rt.ru/support/hometv/setting/tv-box-setup-recommendations': {'первый', 'рекомендация', 'твприставка', 'настройка'},
    'https://spb.rt.ru/support/hometv/setting/hometv-problems': {'интерактивный', 'телевидение', 'работа'},
    'https://spb.rt.ru/support/hometv/setting/instructions': {'инструкция'},
    'https://spb.rt.ru/hometv/equipment': {'оборудование'},
    'https://spb.rt.ru/support/hometv/payment/service-or-equipment-account-payment-methods': {'счёт', 'оплата', 'оборудование', 'выставление', 'порядок', 'услуга'},
    'https://spb.rt.ru/support/hometv/payment/service-or-equipment-payment-amount': {'оплата', 'оборудование', 'узнать', 'услуга', 'сумма'},
    'https://spb.rt.ru/support/phone/payment/invoice-delivery-ways': {'счёт', 'получать'},
    'https://spb.rt.ru/support/phone/payment/find-out-if-payment-has-arrived': {'узнать', 'платёж', 'поступить'},
    'https://spb.rt.ru/support/phone/payment/payment-received-but-no-service': {'платёж', 'поступить', 'не', 'услуга', 'если'},
    'https://spb.rt.ru/support/hometv/reference-information/precautions': {'безопасность', 'мера'},
    'https://spb.rt.ru/support/hometv/reference-information/user-guides': {'пользователь', 'руководство'},
    'https://spb.rt.ru/support/phone/connect/connect-phone-to-house-apartment': {'домашний', 'телефон', 'подключить'},
    'https://spb.rt.ru/support/phone/control/domestic-abroad-calls': {'россия', 'звонок', 'рубеж'},
    'https://spb.rt.ru/support/phone/control/country-city-codes': {'страна', 'город', 'код'},
    'https://spb.rt.ru/support/phone/control/home-phone-number': {'домашний', 'принадлежность', 'телефон', 'номер'},
    'https://spb.rt.ru/support/phone/control/disable-service': {'услуга', 'отключить'},
    'https://spb.rt.ru/support/phone/control/relocation': {'перенести', 'адрес', 'другой', 'переезд', 'услуга'},
    'https://spb.rt.ru/support/phone/contract/change-my-contact-information': {'контактный', 'изменить', 'дать'}}


#  создание dictionary
default_dictionary = {'Как провести интернет в дом или квартиру': 'https://spb.rt.ru/support/internet/connect/conduct-internet-in-house',
    'Как понять, какая скорость интернета мне нужна': 'https://spb.rt.ru/support/internet/connect/what-internet-speed-need',
    'Какие технологии подключения интернета возможны': 'https://spb.rt.ru/support/internet/connect/connection-technologies',
    'Какие действуют тарифы на подключение интернета': 'https://spb.rt.ru/support/internet/connect/tariffs-for-connecting-to-internet',
    'Какие документы нужны для подключения услуги': 'https://spb.rt.ru/support/hometv/connect/documents-required-to-connect-internet',
    'Какое оборудование потребуется для подключения интернета': 'https://spb.rt.ru/support/internet/connect/internet-connection-equipment',
    'Дополнительные возможности при подключении интернета': 'https://spb.rt.ru/support/internet/connect/additional-features-of-home-internet',
    'Как узнать стоимость текущего тарифного плана': 'https://spb.rt.ru/support/phone/connect/find-current-tariff-plan-under-contract',
    'Как узнать скорость по тарифному плану': 'https://spb.rt.ru/support/internet/tariff-service-management/speed-according-to-tariff-plan',
    'Как увеличить скорость интернета': 'https://spb.rt.ru/support/internet/tariff-service-management/increase-internet-speed',
    'Как изменить тарифный план': 'https://spb.rt.ru/support/hometv/control/change-tariff-plan',
    'Как заблокировать услугу на время': 'https://spb.rt.ru/support/phone/control/temporarily-block-service',
    'Как отключить одну из услуг': 'https://spb.rt.ru/support/internet/tariff-service-management/disable-service-without-contract-terminating',
    'Как перенести услугу на другой адрес при переезде': 'https://spb.rt.ru/support/hometv/control/relocation',
    'Как узнать номер лицевого счета': 'https://spb.rt.ru/support/phone/contract/contract-account-number',
    'Как объединить или разделить лицевые счета': 'https://spb.rt.ru/support/phone/contract/combine-separate-account',
    'Как переоформить договор на другого человека': 'https://spb.rt.ru/support/phone/contract/renew-contract-another-person',
    'Как изменить данные о документе, удостоверяющем личность': 'https://spb.rt.ru/support/phone/contract/change-credentials-data',
    'Как изменить контактные данные: номер телефона, е-mail': 'https://spb.rt.ru/support/hometv/contract-management/change-my-contact-information',
    'Согласие на обработку персональных данных': 'https://spb.rt.ru/legal',
    'Как отказаться от уведомлений или рекламы': 'https://spb.rt.ru/support/phone/contract/receive-notifications-or-advertisements',
    'Как отказаться от услуги или расторгнуть договор': 'https://spb.rt.ru/support/hometv/contract-management/how-terminate-contract',
    'Нет доступа к интернету': 'https://spb.rt.ru/support/internet/diagnostics/no-internet-access',
    'Разрывы соединения': 'https://spb.rt.ru/support/internet/diagnostics/connection-breaks',
    'Низкая скорость интернета': 'https://spb.rt.ru/support/internet/diagnostics/low-speed-internet',
    'Все, что нужно знать о Wi-Fi и его скорости': 'https://spb.rt.ru/support/internet/setting/everything-about-wifi-and-speed',
    'Как узнать номер лицевого счета по договору': 'https://spb.rt.ru/support/phone/payment/contract-account-number',
    'Порядок выставления и оплаты счетов за услуги и оборудование': 'https://spb.rt.ru/support/phone/payment/service-or-equipment-account-payment-methods',
    'Как узнать сумму к оплате за услуги и оборудование': 'https://spb.rt.ru/support/phone/payment/service-or-equipment-payment-amount',
    'Какими способами можно получать счета за услуги связи': 'https://spb.rt.ru/support/internet/payment/invoice-delivery-ways',
    'Как оплатить счет': 'https://spb.rt.ru/support/phone/payment/available-payment-methods',
    'Как узнать, поступил ли платеж на счет': 'https://spb.rt.ru/support/internet/payment/find-out-if-payment-has-arrived',
    'Что делать, если платеж поступил, но интернета всё равно нет': 'https://spb.rt.ru/support/internet/payment/payment-received-but-no-internet',
    'Что делать, если платеж не поступил на счет': 'https://spb.rt.ru/support/phone/payment/payment-has-not-been-received',
    'Как подключить автоплатеж': 'https://spb.rt.ru/support/phone/payment/how-to-enable-auto-payment',
    'Как вернуть остаток денежных средств безналичным способом': 'https://spb.rt.ru/support/phone/payment/how-return-balance-of-funds-using-non-cash-method',
    'Как перенести платеж между лицевыми счетами': 'https://spb.rt.ru/support/phone/payment/how-transfer-payment-between-personal-accounts',
    'Как подключить обещанный платеж': 'https://spb.rt.ru/support/phone/payment/how-to-activate-promised-payment',
    'Договоры и соглашения': 'https://spb.rt.ru/support/documents#phone',
    'Как стать клиентом Ростелекома': 'https://spb.rt.ru/support/mobile/connect/become-client-rostelecom',
    'Переход в «Ростелеком» со своим номером': 'https://spb.rt.ru/support/mobile/connect/transition-rostelecom-with-your-number',
    'Форма оплаты': 'https://spb.rt.ru/support/mobile/payment/form-of-payment',
    'Баланс и оплата': 'https://spb.rt.ru/support/mobile/payment/balance-and-payment',
    'Тарифный план': 'https://spb.rt.ru/mobile/mobile_tariff',
    'Услуги': 'https://spb.rt.ru/support/mobile/control/services',
    'SIM-карта и номер телефона': 'https://spb.rt.ru/support/mobile/control/sim-card-and-phone-number',
    'Порядок набора номера': 'https://spb.rt.ru/support/mobile/control/order-of-dialing',
    'Обработка персональных данных': 'https://spb.rt.ru/legal',
    'Как расторгнуть договор': 'https://spb.rt.ru/support/phone/contract/terminate-contract',
    'Программа Бонус': 'https://spb.rt.ru/bonus',
    'Настройки для мобильного интернета': 'https://spb.rt.ru/support/mobile/setting/settings-mobile-internet',
    'Настройки для мобильного интернета в роуминге': 'https://spb.rt.ru/support/mobile/setting/settings-mobile-internet-roaming',
    'Самообслуживание': 'https://spb.rt.ru/support/mobile/reference-information/self-service',
    'Справочники и документы': 'https://spb.rt.ru/support/documents#mobile',
    'Зона покрытия': 'https://spb.rt.ru/mobile/mobile_tariff#zone',
    'Как подключить Интерактивное ТВ в доме или квартире': 'https://spb.rt.ru/support/hometv/connect/connect-tv-to-house-apartment',
    'Что такое Интерактивное ТВ': 'https://spb.rt.ru/support/hometv/connect/what-is-interactive-tv',
    'Какие технологии подключения Интерактивного ТВ возможны': 'https://spb.rt.ru/support/hometv/connect/interactive-tv-connection-technologies',
    'Какие действуют тарифы на подключение Интерактивного ТВ': 'https://spb.rt.ru/support/hometv/connect/tariffs-for-connecting-television',
    'Какое оборудование потребуется для подключения Интерактивного ТВ': 'https://spb.rt.ru/support/hometv/connect/television-connection-equipment',
    'Дополнительные возможности при подключении Интерактивного ТВ': 'https://spb.rt.ru/support/hometv/connect/additional-features-of-home-television',
    'Как узнать, что входит в состав пакета Интерактивного ТВ': 'https://spb.rt.ru/support/hometv/control/interactive-tv-package-what-is-included',
    'Как настроить «Мультискрин» для Wink': 'https://spb.rt.ru/support/hometv/control/multiscreen',
    'Как подключить или отключить дополнительные опции Интерактивного ТВ': 'https://spb.rt.ru/support/hometv/control/disable-service',
    'Рекомендации по первой настройке ТВ-приставки': 'https://spb.rt.ru/support/hometv/setting/tv-box-setup-recommendations',
    'Проблемы с работой Интерактивного телевидения': 'https://spb.rt.ru/support/hometv/setting/hometv-problems',
    'Инструкции': 'https://spb.rt.ru/support/hometv/setting/instructions',
    'Оборудование': 'https://spb.rt.ru/hometv/equipment',
    'Порядок выставления и оплаты счетов за услугу и оборудование': 'https://spb.rt.ru/support/hometv/payment/service-or-equipment-account-payment-methods',
    'Как узнать сумму к оплате за услуги или оборудование': 'https://spb.rt.ru/support/hometv/payment/service-or-equipment-payment-amount',
    'Как получать счета': 'https://spb.rt.ru/support/phone/payment/invoice-delivery-ways',
    'Как узнать, поступил ли платеж': 'https://spb.rt.ru/support/phone/payment/find-out-if-payment-has-arrived',
    'Что делать, если платеж поступил, но услуга не работает': 'https://spb.rt.ru/support/phone/payment/payment-received-but-no-service',
    'Меры безопасности': 'https://spb.rt.ru/support/hometv/reference-information/precautions',
    'Руководства пользователя': 'https://spb.rt.ru/support/hometv/reference-information/user-guides',
    'Как подключить домашний телефон': 'https://spb.rt.ru/support/phone/connect/connect-phone-to-house-apartment',
    'Звонки по России и за рубеж': 'https://spb.rt.ru/support/phone/control/domestic-abroad-calls',
    'Коды стран и городов': 'https://spb.rt.ru/support/phone/control/country-city-codes',
    'Принадлежность домашнего номера телефона': 'https://spb.rt.ru/support/phone/control/home-phone-number',
    'Как отключить услугу': 'https://spb.rt.ru/support/phone/control/disable-service',
    'Как перенести услугу на другой адрес при переезде ': 'https://spb.rt.ru/support/phone/control/relocation',
    'Как изменить контактные данные': 'https://spb.rt.ru/support/phone/contract/change-my-contact-information'}
from keywords import key_words
if __name__ == '__main__':
    for i in dictionary:
        set_return = set()
        for j in key_words(i):
            set_return.add(j)
        print(f"'{dictionary[i]}': {set_return}")