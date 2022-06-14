# program untuk menghitung kecepatan Angin dan suhu :

# Angin
def conv_angin(celcius):
    convert_angin = 4 * celcius / 5
    return convert_angin
 
# convert celcius to farenheit
def conv_farenheit(celcius):
    convert_farenheit = 9 * celcius / 5 + 32
    return convert_farenheit
 
# convert celcius to kelvin
def conv_kelvin(celcius):
    convert_kelvin = celcius + 273
    return convert_kelvin
 
# create main menu
def main():
    print('Program Tanggap Bencana')
    print('=======================')
    print('Peduli Sesama.com')
 
    # create input
    temperature = int(input('Masukan Skala : '))
 
    # cetak hasil
    print('++++++++++++++++++++++++++++++++++++++++++++')
    print(f'Hasil Konnversi kecepatan angin {temperature} adalah {conv_angin(temperature)} km/jam')
    print(f'Hasil Konversi suhu farenheit  {temperature} adalah {conv_farenheit(temperature)} Farenheit')
    print(f'Hasil Konversi suhu kelvin {temperature} adalah {conv_kelvin(temperature)} Kelvin')
    print('++++++++++++++++++++++++++++++++++++++++++++++')
    
 
if __name__=='__main__':
    main()
