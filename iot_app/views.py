import logging

from django.shortcuts import render

logger = logging.getLogger(__name__)


def index(request):
    logger.debug('debug from index')
    return render(request, 'index.html')
