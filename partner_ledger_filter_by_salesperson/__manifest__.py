# -*- coding: utf-8 -*-
{
    'name': "partner_ledger_filter_by_salesperson",
    'description': "This module adds a filter by salesperson to the partner ledger report. It includes features like filtering, exporting reports with salesperson data, and seamless integration with existing reports.",
    'category': 'Addon',
    'author': "Odoo Developers",
    'version': '15.0',
    'depends': ['base', 'account_accountant', 'account_reports'],
    'license': 'LGPL-3',
    'data': [
        'views/partner_ledger_view.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'partner_ledger_filter_by_salesperson/static/src/js/partner_ledger_filter.js',
        ],
    },
    'price': 30.00,

    'currency': 'USD',
    'images': ['static/description/icon.png', 'static/description/cover_image.png'],
}
