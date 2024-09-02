import plotly.graph_objects as go

fig = go.Figure(go.Sankey(
    arrangement='snap',
    node=dict(
        label=['Giriş', 'Sebze Reyonu', 'Et Reyonu', 'Atıştırmalık Reyonu', 'Kişisel Bakım Reyonu', 'Kasa', 'Çıkış'],
        x=[0.1, 0.2, 0.4, 0.4, 0.4, 0.4, 0.2],
        y=[0.7, 0.7, 0.7, 0.6, 0.5, 0.2, 0.2],
        pad=10,

    ),
    link=dict(
        arrowlen=15,
        source=[0, 1, 2, 3, 1, 4, 1, 5],
        target=[1, 2, 3, 1, 4, 1, 5, 6],
        value=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
    )
    ))

fig.show()
