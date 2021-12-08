# Layout / Responsive
from ctypes import alignment
from h2o_wave import site, ui , data
import time
import psutil
import json

page = site['/covid']
page.drop()

# Used meta for different viewport sizes of browser.
page['meta'] = ui.meta_card(box='', layouts=[
    ui.layout(
        # If the viewport width >= 0:
        breakpoint='xs',
        zones=[
            ui.zone('header', size='80px'),
            # Use remaining space for content
            ui.zone('content'),
            ui.zone('center'),
            ui.zone('cards'),
            ui.zone('daily')
        ]
    ),
    ui.layout(
        # If the viewport width >= 768:
        breakpoint='m',
        zones=[
            # 80px high header
            ui.zone('header', size='80px'),
            # Use remaining space for body
           ui.zone('graphs', direction=ui.ZoneDirection.ROW),
            ui.zone('cards', direction=ui.ZoneDirection.ROW, align='start',justify='start'),
            ui.zone('dailyRow', direction=ui.ZoneDirection.ROW, align='start',justify='start'),
            ui.zone('footer'),
        ]
    ),
    ui.layout(
        # If the viewport width >= 1200:
        breakpoint='xl',
        width='1200px',
        zones=[
            # 80px high header
            ui.zone('header', size='80px'),
            # Use remaining space for body
            
            ui.zone('graphs', direction=ui.ZoneDirection.ROW),
            ui.zone('cards', direction=ui.ZoneDirection.ROW, align='start',justify='start'),
            ui.zone('dailyRow', direction=ui.ZoneDirection.ROW, align='start',justify='start'),
            ui.zone('footer'),
            
        ]
    )
])
# Defining header
page['header'] = ui.header_card(
    # Place card in the header zone, regardless of viewport size.
    box='header',
    title='Covid19 Dashboard',
    subtitle='Realtime order Covid19 Cases Tracker',
    
   
)

#Defining footer
page['footer'] = ui.footer_card(box='footer', caption='(c) H2O Interview Task ')

#Defining arrival rate graphs
page['center1'] = ui.small_series_stat_card(
    box=ui.boxes(
        # If the viewport width >= 0, place as fourth item in content zone.
        ui.box(zone='center', order=1),
        # If the viewport width >= 768, place as third item in content zone.
       ui.box(zone='graphs', order=2, size=1),
        # If the viewport width >= 1200, place in content zone.
        ui.box(zone='graphs', order=2, size=1),
    ),
    title='New Cases Arrival Rate',
    value='={{usage}}%',
    data=dict(usage=0.0),
    plot_data=data('tick usage', -15),
    plot_category='tick',
    plot_value='usage',
    plot_zero_value=0,
    plot_color='$red',
)

#Defining arrival rate graphs
page['center2'] = ui.small_series_stat_card(
    box=ui.boxes(
        # If the viewport width >= 0, place as fourth item in content zone.
        ui.box(zone='center', order=2),
        # If the viewport width >= 768, place as third item in content zone.
        ui.box(zone='graphs', order=1, size=1),
        # If the viewport width >= 1200, place in content zone.
        ui.box(zone='graphs', order=1, size=1),
    ),
    title='Overall Cases Arrival Rate',
    value='={{usage}}%',
    data=dict(usage=0.0),
    plot_data=data('tick usage', -15),
    plot_category='tick',
    plot_value='usage',
    plot_zero_value=0,
    plot_color='$blue',
)
#Defining cards
page['card1'] = ui.small_stat_card(
    box=ui.boxes(
                # If the viewport width >= 0, place as fourth item in content zone.
                ui.box(zone='cards', order=4),
                # If the viewport width >= 768, place as third item in content zone.
                ui.box(zone='cards', order=3),
                # If the viewport width >= 1200, place in content zone.
                ui.box(zone='cards', order=2, size=1),
            ),
    title= 'Today Cases',
    value='442',
)
#Defining cards
page['card2'] = ui.small_stat_card(
    box=ui.boxes(
                # If the viewport width >= 0, place as fourth item in content zone.
                ui.box(zone='cards', order=4),
                # If the viewport width >= 768, place as third item in content zone.
                ui.box(zone='cards', order=3),
                # If the viewport width >= 1200, place in content zone.
                ui.box(zone='cards', order=2, size=1),
            ),
    title= 'Today Deads',
    value='24',
)
#Defining cards
page['card3'] = ui.small_stat_card(
    box=ui.boxes(
                # If the viewport width >= 0, place as fourth item in content zone.
                ui.box(zone='cards', order=4),
                # If the viewport width >= 768, place as third item in content zone.
                ui.box(zone='cards', order=3),
                # If the viewport width >= 1200, place in content zone.
                ui.box(zone='cards', order=2, size=1),
            ),
    title= 'Today Recovers',
    value='398',
)
#Defining cards
page['card4'] = ui.small_stat_card(
    box=ui.boxes(
                # If the viewport width >= 0, place as fourth item in content zone.
                ui.box(zone='cards', order=4),
                # If the viewport width >= 768, place as third item in content zone.
                ui.box(zone='cards', order=3),
                # If the viewport width >= 1200, place in content zone.
                ui.box(zone='cards', order=2, size=1),
            ),
    title= 'Overall patients',
    value='152038',
)
# Difining arguments for chart
spec_linear_scale = json.dumps(dict(
    mark='bar',
    encoding=dict(
        x=dict(field='count', type='ordinal'),
        y=dict(field='days', type='quantitative')
    )
))

plot_data = data(fields=["count", "days"], rows=[
    ["Nov 29", 28], ["Nov 30", 55], ["Dec 1", 43],
    ["Dec 2", 91], ["Dec 3", 81], ["Dec 4", 53],
    ["Dec 5", 19], ["Dec 6", 87], ["Dec 7", 52]
], pack=True)

plot_dataG = data(fields=["count", "days"], rows=[
    ["Nov 29", 1000], ["Nov 30", 1005], ["Dec 1", 1500],
    ["Dec 2", 2431], ["Dec 3", 1567], ["Dec 4", 2192],
    ["Dec 5", 1232], ["Dec 6", 2314], ["Dec 7", 1121]
], pack=True)

linear_scale_command = ui.command(
    name='to_linear_scale',
    label='Linear Scale',
    icon='LineChart',
)

page['daily'] = ui.form_card(
            box=ui.boxes(
                # If the viewport width >= 0, place as fourth item in content zone.
                ui.box(zone='cards', order=4),
                # If the viewport width >= 768, place as third item in content zone.
                ui.box(zone='dailyRow', order=1, size=1),
                # If the viewport width >= 1200, place in content zone.
                ui.box(zone='dailyRow', order=1, size=1),
            ),
            items=[
                ui.text_l(content='Daily Cases in Sri Lanka', commands=[linear_scale_command]),
                ui.vega_visualization(specification=spec_linear_scale, data=plot_data, height='300px'),
            ],
        )

page['dailyGlobal'] = ui.form_card(
            box=ui.boxes(
                # If the viewport width >= 0, place as fourth item in content zone.
                ui.box(zone='cards', order=4),
                # If the viewport width >= 768, place as third item in content zone.
                ui.box(zone='dailyRow', order=2, size=1),
                # If the viewport width >= 1200, place in content zone.
                ui.box(zone='dailyRow', order=2, size=1),
            ),
            items=[
                ui.text_l(content='Daily Cases in Global', commands=[linear_scale_command]),
                ui.vega_visualization(specification=spec_linear_scale, data=plot_dataG, height='300px'),
            ],
        )
 
 #Getting CPU usage
tick = 0
while True:
    tick += 1

    cpu_usage = psutil.cpu_percent(interval=1)
    mem_usage = psutil.virtual_memory().percent
    page['center2'].data.usage = cpu_usage
    page['center1'].data.usage = mem_usage
    
    page['center2'].plot_data[-1] = [tick, cpu_usage]
    page['center1'].plot_data[-1] = [tick, mem_usage]

    page.save()
    time.sleep(1)
