numbers = [
    {'firstSurah': f'3', 'firstAyah': '31', 'secondSurah': f'33', 'secondAyah': '1'},
    {'firstSurah': f'33', 'firstAyah': '1', 'secondSurah': f'3', 'secondAyah': '31'},
    {'firstSurah': f'1', 'firstAyah': '10', 'secondSurah': f'11', 'secondAyah': '1'},
    {'firstSurah': f'1', 'firstAyah': '12', 'secondSurah': f'11', 'secondAyah': '2'},
    {'firstSurah': f'1', 'firstAyah': '13', 'secondSurah': f'11', 'secondAyah': '3'},
    {'firstSurah': f'1', 'firstAyah': '14', 'secondSurah': f'11', 'secondAyah': '4'},
    {'firstSurah': f'1', 'firstAyah': '15', 'secondSurah': f'11', 'secondAyah': '5'},
    {'firstSurah': f'1', 'firstAyah': '16', 'secondSurah': f'11', 'secondAyah': '6'},
    {'firstSurah': f'1', 'firstAyah': '17', 'secondSurah': f'11', 'secondAyah': '7'},
    {'firstSurah': f'1', 'firstAyah': '18', 'secondSurah': f'11', 'secondAyah': '8'},
    {'firstSurah': f'1', 'firstAyah': '19', 'secondSurah': f'11', 'secondAyah': '9'},
    {'firstSurah': f'1', 'firstAyah': '21', 'secondSurah': f'12', 'secondAyah': '1'},
    {'firstSurah': f'1', 'firstAyah': '22', 'secondSurah': f'12', 'secondAyah': '2'},
    {'firstSurah': f'1', 'firstAyah': '23', 'secondSurah': f'12', 'secondAyah': '3'},
    {'firstSurah': f'1', 'firstAyah': '24', 'secondSurah': f'12', 'secondAyah': '4'},
    {'firstSurah': f'1', 'firstAyah': '25', 'secondSurah': f'12', 'secondAyah': '5'},
    {'firstSurah': f'1', 'firstAyah': '26', 'secondSurah': f'12', 'secondAyah': '6'},
    {'firstSurah': f'1', 'firstAyah': '27', 'secondSurah': f'12', 'secondAyah': '7'},
    {'firstSurah': f'1', 'firstAyah': '28', 'secondSurah': f'12', 'secondAyah': '8'},
    {'firstSurah': f'1', 'firstAyah': '29', 'secondSurah': f'12', 'secondAyah': '9'},
    {'firstSurah': f'1', 'firstAyah': '31', 'secondSurah': f'13', 'secondAyah': '1'},
    {'firstSurah': f'1', 'firstAyah': '32', 'secondSurah': f'13', 'secondAyah': '2'},
    {'firstSurah': f'1', 'firstAyah': '33', 'secondSurah': f'13', 'secondAyah': '3'},
    {'firstSurah': f'1', 'firstAyah': '34', 'secondSurah': f'13', 'secondAyah': '4'},
    {'firstSurah': f'1', 'firstAyah': '35', 'secondSurah': f'13', 'secondAyah': '5'},
    {'firstSurah': f'1', 'firstAyah': '36', 'secondSurah': f'13', 'secondAyah': '6'},
    {'firstSurah': f'1', 'firstAyah': '37', 'secondSurah': f'13', 'secondAyah': '7'},
    {'firstSurah': f'1', 'firstAyah': '38', 'secondSurah': f'13', 'secondAyah': '8'},
    {'firstSurah': f'1', 'firstAyah': '39', 'secondSurah': f'13', 'secondAyah': '9'},
    {'firstSurah': f'1', 'firstAyah': '41', 'secondSurah': f'14', 'secondAyah': '1'},
    {'firstSurah': f'1', 'firstAyah': '42', 'secondSurah': f'14', 'secondAyah': '2'},
    {'firstSurah': f'1', 'firstAyah': '43', 'secondSurah': f'14', 'secondAyah': '3'},
    {'firstSurah': f'1', 'firstAyah': '44', 'secondSurah': f'14', 'secondAyah': '4'},
    {'firstSurah': f'1', 'firstAyah': '45', 'secondSurah': f'14', 'secondAyah': '5'},
    {'firstSurah': f'1', 'firstAyah': '46', 'secondSurah': f'14', 'secondAyah': '6'},
    {'firstSurah': f'1', 'firstAyah': '47', 'secondSurah': f'14', 'secondAyah': '7'},
    {'firstSurah': f'1', 'firstAyah': '48', 'secondSurah': f'14', 'secondAyah': '8'},
    {'firstSurah': f'1', 'firstAyah': '49', 'secondSurah': f'14', 'secondAyah': '9'},
]

newList = []
for item in numbers:
    for secItem in numbers:
        if item["firstSurah"] == secItem["secondSurah"] or (item["firstSurah"] != secItem["secondSurah"] and item["firstAyah"] != secItem["firstAyah"]):
            pass
        else:
            newList.append(item)

with open("newFile.txt", "w") as file:
    for item in newList:
        file.write(f"{item}\n")