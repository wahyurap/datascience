from datetime import datetime
import random
nama = "Wahyu"
tanggal = datetime.now().day
default = "maaf, aku tidak tahu jawaban dari pertanyaanmu"

jawaban_nama = [
    "nama saya  {0}".format(nama),
    "orang-orang memanggil saya {0}".format(nama),
    "panggil saja saya {0}".format(nama)
]

jawaban_tanggal = [
    "hari ini tanggal {0}".format(tanggal),
    "ya ampun masa tidak tahu, hari ini tanggal".format(tanggal)
]

pertanyaan = {
    "nama kamu siapa?": jawaban_nama,
    "kamu siapa?": jawaban_nama,
    "tanggal berapa hari ini?": jawaban_tanggal,
    "hari ini tanggal berapa?": jawaban_tanggal,
    "default": default
}

statement = [
    'ceritakan lebih banyak!',
    'kenapa kamu berpikir begitu?',
    'sudah berapa lama kamu merasa seperti ini?',
    'Itu sangat menarik!',
    'oh wow!',
    ':)'
]

responses = {
    'pertanyaan': pertanyaan,
    'statement': statement
}



def chatbot(message):
    a= ''
    print('Saya :',message)
    if "?" in message:
        if 'siapa' in message:
            a = random.choices(jawaban_nama)
        elif 'hari' in message:
            a =random.choices(jawaban_tanggal)
        else:
            a = default
    else:
        a = random.choices(statement)
    return str(a).strip("'[]")

print(chatbot('Selamat Pagi'))
print(chatbot('Mau bermain bersamaku?'))
print(chatbot('nama kamu siapa?'))
print(chatbot('hari ini tanggal berapa?'))

