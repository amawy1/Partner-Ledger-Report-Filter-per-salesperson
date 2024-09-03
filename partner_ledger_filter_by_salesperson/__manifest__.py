# -*- coding: utf-8 -*-
{
    'name': "partner_ledger_filter_by_salesperson",
    'description': """
<h1>Partner Ledger Filter by Salesperson</h1>
<p>This module enhances the Odoo accounting system by adding a filter option for salespersons in the partner ledger report. It's designed to help businesses better analyze and manage their sales data.</p>

<h2>Key Features:</h2>
<ul>
    <li><strong>Salesperson Column:</strong> Adds a new column in the partner ledger report to display the salesperson associated with each entry.</li>
    <li><strong>Filter by Salesperson:</strong> Allows users to filter the partner ledger report by salesperson, providing a more focused view of sales activities.</li>
    <li><strong>Export with Salesperson:</strong> Enables exporting the filtered report with salesperson details for further analysis.</li>
    <li><strong>Seamless Integration:</strong> Integrates smoothly with existing accounting reports in Odoo.</li>
    <li><strong>Compatibility:</strong> Fully compatible with Odoo 15.0.</li>
</ul>

<h2>Benefits:</h2>
<ul>
    <li>Improves sales analysis by providing detailed insights based on salespersons.</li>
    <li>Helps managers and accountants make data-driven decisions with accurate reporting.</li>
    <li>Saves time by offering an easy-to-use filtering option directly in the partner ledger report.</li>
</ul>

<h2>Installation:</h2>
<p>Follow the standard Odoo module installation process. No additional configuration is required after installation.</p>

<h2>Support:</h2>
<p>If you encounter any issues or have questions, feel free to contact our support team.</p>
""",

    'category': 'Accounting',
    'author': "Odoo Developer",
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
