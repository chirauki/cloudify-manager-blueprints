#!/usr/bin/env python

from os.path import join, dirname

from cloudify import ctx

ctx.download_resource(
    join('components', 'utils.py'),
    join(dirname(__file__), 'utils.py'))
import utils  # NOQA

STAGE_SERVICE_NAME = 'stage'


if 'skip_installation' not in ctx.instance.runtime_properties:
    ctx.logger.info('Starting Stage (UI) Service...')
    utils.start_service(STAGE_SERVICE_NAME)
