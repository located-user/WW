from django.shortcuts import render
from .form import Form
#from.models import Data
from . Code import WW_algo
# Create your views here.
def Home(request):
    if request.method == "POST":
        form = Form(request.POST)
        if form.is_valid():
            NB = form.cleaned_data['NB']
            t = float(form.cleaned_data['taux_passation'])
            cc = form.cleaned_data['Cout_Commande']
            p = request.POST.getlist('p', [])
            pr = request.POST.getlist('pr', [])
            # Convertir les valeurs en entiers si nécessaire
            p = [int(val) for val in p if val.strip()]
            pr = [int(val) for val in pr if val.strip()]
            c =WW_algo(p, pr, cc, t)
            prix_min, methode=c
            context = {
                'form': form,
                'NB':NB,
                'prix_min': prix_min,
                'methode': methode
            }
            return render(request, 'WW/Affichage.html',context)  # Transmettre le contexte à la page WW/Affichage.html
    else:
        form = Form()
    return render(request, 'WW/Home.html', {'form': form})




"""def Data(request):
    if request.method == "POST":
        form = Form(request.POST)
        if form.is_valid():
            NB=form.cleaned_data['NB']
            pr=form.cleanedData['prix_achat']
            t=form.cleanedData['taux_passation']
            cc=form.cleanedData['Cout_Commande']
            p=[]
            for i in range(NB):
                p0=form.cleanedData[f'Periode_data_{i}']
                p.append(p0)    
            prix_min,_,methode=WW_algo(p,pr,cc,t)
            context = {
                form:'form',
                NB:'NB',
                pr:'prix',
                t:'t',
                cc:'cc',
                p:'p',
                prix_min:'prix_min',
                methode:'methode'
            }
        return render(request, 'WW/Home.html', context)
    else:
        return render(request, 'WW/Home.html', context)

"""

