from django.http import HttpResponse
from django.template import loader
from .models import Pokemon, Trainer

def index(request):
    pokemons = Pokemon.objects.all()
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'pokemons': pokemons}, request))

def pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id = pokemon_id)
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))

##################################
def trainers(request):
    trainers = Trainer.objects.all()
    template = loader.get_template('index_trainers.html')
    return HttpResponse(template.render({'trainers': trainers}, request))

def trainer(request, trainer_id):
    trainer = Trainer.objects.get(id=trainer_id)
    template = loader.get_template('display_trainers.html')
    context = {'trainer': trainer}
    return HttpResponse(template.render(context, request))