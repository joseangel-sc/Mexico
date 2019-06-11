from collections import namedtuple

name = "states"

"""
Mexican states definition.

Ref. https://en.wikipedia.org/wiki/List_of_states_of_Mexico
"""

State = namedtuple('State', ['name', 'official_name', 'capital', 'largest_city', 'area', 'population'])

STATES = [
    State('Aguascalientes', 'Aguascalientes', 'Aguascalientes', 'Aguascalientes', 5_618, 1_184_996),
    State('Baja California', 'Baja California', 'Mexicali', 'Tijuana', 71_446, 3_155_070),
    State('Baja California Sur', 'Baja California Sur', 'La Paz', 'La Paz', 73_922, 637_026),
    State('Campeche', 'Campeche', 'San Francisco de Campeche', 'San Francisco de Campeche', 57_924, 822_441),
    State('Chiapas', 'Chiapas', 'Tuxtla Gutiérrez', 'Tuxtla Gutiérrez', 73_289, 4_796_580),
    State('Mexico City', 'Ciudad de México', '', '', 1_495, 8_918_653),
    State('Chihuahua', 'Chihuahua', 'Chihuahua', 'Ciudad Juárez', 247_455, 3_406_465),
    State('Coahuila', 'Coahuila de Zaragoza', 'Saltillo', 'Saltillo', 151_563, 2_748_391),
    State('Colima', 'Colima', 'Colima', 'Manzanillo', 5_625, 650_555),
    State('Durango', 'Durango', 'Victoria de Durango', 'Victoria de Durango', 123_451, 1_632_934),

    State('Guanajuato', 'Guanajuato', 'Guanajuato', 'León', 30_608, 5_486_372),
    State('Guerrero', 'Guerrero', 'Chilpancingo de los Bravo', 'Acapulco', 63_621, 3_388_768),
    State('Hidalgo', 'Hidalgo', 'Pachuca', 'Pachuca', 20_846, 2_665_018 ),
    State('Jalisco', 'Jalisco', 'Guadalajara', 'Guadalajara', 78_599, 7_350_682),
    State('México', 'México', 'Toluca de Lerdo', 'Ecatepec de Morelos', 22_357, 15_175_862),
    State('Morelos', 'Morelos', 'Cuernavaca', 'Cuernavaca', 4_893, 1_777_227),
    State('Nayarit', 'Nayarit', 'Tepic', 'Tepic', 27_815, 1_084_979),
    State('Nuevo León', 'Nuevo León', 'Monterrey', 'Monterrey', 64_220, 4_653_458),
    State('Oaxaca', 'Oaxaca', 'Oaxaca de Juárez', 'Oaxaca de Juárez', 93_793, 3_801_962),
    State('Puebla', 'Puebla', 'Puebla de Zaragoza','Puebla de Zaragoza', 34_290, 5_779_829),

    State('Querétaro', 'Querétaro de Arteaga', 'Santiago de Querétaro', 'Santiago de Querétaro', 11_684, 1_827_937),
    State('Quintana Roo', 'Quintana Roo', 'Chetumal', 'Cancún', 42_361, 1_325_578),
    State('San Luis Potosí', 'San Luis Potosí', 'San Luis Potosí', 'San Luis Potosí', 60_983, 2_585_518),
    State('Sinaloa', 'Sinaloa', 'Culiacán', 'Culiacán', 57_377, 2_767_761),
    State('Sonora',  'Sonora', 'Hermosillo', 'Hermosillo', 179_503, 2_662_480),
    State('Tabasco', 'Tabasco',	'Villahermosa',	'Villahermosa',	24_738, 2_238_603),
    State('Tamaulipas', 'Tamaulipas', 'Ciudad Victoria', 'Reynosa',	80_175, 3_268_554),
    State('Tlaxcala', 'Tlaxcala', 'Tlaxcala', 'Vicente Guerrero',	3_991, 1_169_936),
    State('Veracruz', 'Veracruz de Ignacio de la Llave', 'Xalapa', 'Veracruz', 71_820, 7_643_194),
    State('Yucatán', 'Yucatán', 'Mérida', 'Mérida', 39_612, 1_955_577),

    State('Zacatecas', 'Zacatecas', 'Zacatecas', 'Zacatecas', 75_539, 1_490_668)
    ]

