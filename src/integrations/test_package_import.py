#!/usr/bin/env python3  # noqa: CPY001
"""Test script to verify package functionality."""

import time

try:
    # Test imports
    from yeeti.zero_spinner import Spinner, spinner

    print(f'✓ Successfully imported spinner: {spinner.__name__}')
    print(f'✓ Successfully imported Spinner: {Spinner.__name__}')

    # Test main functionality
    spin = spinner()
    print(f'✓ Spinner created successfully from {spinner.__name__}')
    spin = Spinner()
    print(f'✓ Spinner created successfully from {Spinner.__name__}')

    # Test spinning
    spin = spinner()
    spin.start('Start spinning...')
    time.sleep(2)
    spin.succeed('End spinning!')
    print('✓ Spinner spinning successfully')

    print('✓ All tests passed!')

except ImportError as e:
    print(f'✗ Import error: {e}')
except Exception as e:
    print(f'✗ Runtime error: {e}')
