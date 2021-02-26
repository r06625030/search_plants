from .models import Plants
from django.db.models import Q


def plantsFilter(formdata):
    queryset = Plants.objects.filter(
        Q(fName__icontains=formdata['family']) | Q(gName__icontains=formdata['family']),
        Q(cName__icontains=formdata['name']) | Q(aName__icontains=formdata['name']),
        Q(sName__icontains=formdata['sName']) | Q(gName__icontains=formdata['sName']),
        Q(stem__icontains=formdata['stemType']),
        Q(leaf__icontains=formdata['phyllotaxy']),
        Q(leaf__icontains=formdata['leafOther']),
    )
    if formdata['leafType'] == '單葉':
        queryset = queryset.exclude(Q(leaf__icontains='複葉'))
    else:
        queryset = queryset.filter(Q(leaf__icontains=formdata['leafType']))
    if formdata['flowerColor'] == '橙':
        queryset = queryset.filter(Q(flower__icontains='橙') | Q(flower__icontains='橘'))
    else:
        queryset = queryset.filter(Q(flower__icontains=formdata['flowerColor']))
    if formdata['inflorescence'] == '肉穗':
        queryset = queryset.filter(Q(flower__icontains='肉穗') | Q(flower__icontains='佛焰花序'))
    elif formdata['inflorescence'] == '單生':
        queryset = queryset.exclude(Q(flower__icontains='花序'))
    else:
        queryset = queryset.filter(Q(flower__icontains=formdata['inflorescence']))
    if formdata['fruit'] == '隱花果':
        queryset = queryset.filter(Q(fruit__icontains='隱花') | Q(fruit__icontains='隱頭') | Q(fruit__icontains='榕果'))
    else:
        queryset = queryset.filter(Q(fruit__icontains=formdata['fruit']))

    queryset = queryset.order_by('fName')
    # 把queryset做成依照科別分類的字典
    output = dict()
    for plant in queryset:
        if plant.fName not in output:
            output[plant.fName] = []
        output[plant.fName].append(plant)
    return output