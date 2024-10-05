
from django.shortcuts import render
from django.db.models import Sum
from .models import AnnouncedLGAResult

def calculate_total_votes(request):
    # Sum all the votes (party_score) across all announced LGA results
    total_votes = AnnouncedLGAResult.objects.aggregate(total=Sum('party_score'))['total']
    
    context = {
        'total_votes': total_votes
    }
    
    return render(request, 'results/total_votes.html', context)