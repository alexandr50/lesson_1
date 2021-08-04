duration = int(input())
days = duration // (24 * 3600)
hour = (duration % (24 * 3600)) // 3600
minutes = ((duration % (24 * 3600)) % 3600) // 60
seconds = duration % 60
print(seconds, 'сек')
print(minutes, 'мин')
print(hour, 'час')
print(days, 'дня')
