from django import forms


class SearchForm(forms.Form):
    STEM = [
        ('', '不指定'),
        ('喬木', '喬木'),
        ('灌木', '灌木'),
        ('草本', '草本'),
        ('藤本', '藤本')
    ]
    LEAF_T = [
        ('', '不指定'),
        ('單葉', '單葉'),
        ('裂葉', '裂葉'),
        ('複葉', '複葉'),
        ('單身複葉', '單身複葉'),
        ('羽狀複葉', '羽狀複葉'),
        ('掌狀複葉', '掌狀複葉'),
    ]
    LEAF_P = [
        ('', '不指定'),
        ('互生', '互生'),
        ('對生', '對生'),
        ('輪生', '輪生'),
        ('基生', '基生'),
        ('叢生', '叢生'),
    ]
    FLOWER_I = [
        ('', '不指定'),
        ('單生', '單生'),
        ('總狀', '總狀花序'),
        ('繖房', '繖房花序'),
        ('繖形', '繖形花序'),
        ('頭狀', '頭狀花序'),
        ('隱頭', '隱頭花序'),
        ('穗狀', '穗狀花序'),
        ('柔荑', '柔荑花序'),
        ('肉穗', '肉穗/佛焰花序'),
        ('聚繖', '聚繖花序'),
        ('大戟', '大戟花序'),
    ]
    FLOWER_C = [
        ('', '不指定'),
        ('紅', '紅'),
        ('橙', '橙'),
        ('黃', '黃'),
        ('藍', '藍'),
        ('紫', '紫'),
    ]
    FRUIT = [
        ('', '不指定'),
        ('漿果', '漿果'), ('核果', '核果'), ('仁果', '仁果'), ('柑果', '柑果'), ('瓠果', '瓠果'),
        ('蓇葖果', '蓇葖果'), ('莢果', '莢果'), ('角果', '角果'), ('蒴果', '蒴果'), ('瘦果', '瘦果'),
        ('穎果', '穎果'), ('胞果', '胞果'), ('翅果', '翅果'), ('堅果', '堅果'), ('離果', '離果'),
        ('隱花果', '隱花果'), ('孢子', '孢子'),
    ]
    family = forms.CharField(label='科別（中或英文）', max_length=10, required=False,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(label='植物名稱（中或英文）', max_length=10, required=False,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    sName = forms.CharField(label='學名', max_length=10, required=False,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    stemType = forms.ChoiceField(label='外型', choices=STEM, required=False,
                                 widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
    leafType = forms.ChoiceField(label='葉型態', choices=LEAF_T, required=False,
                                 widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
    phyllotaxy = forms.ChoiceField(label='葉序', choices=LEAF_P, required=False,
                                 widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
    leafOther = forms.CharField(label='其他葉特徵描述', max_length=10, required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    inflorescence = forms.ChoiceField(label='花序', choices=FLOWER_I, required=False,
                                 widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
    flowerColor = forms.ChoiceField(label='花色', choices=FLOWER_C, required=False,
                                 widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
    fruit = forms.ChoiceField(label='果實', choices=FRUIT, required=False,
                                 widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
