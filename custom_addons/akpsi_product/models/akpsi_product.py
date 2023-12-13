import logging

from odoo import fields, models, api, _
from odoo.exceptions import UserError, ValidationError


class AKPSIProduct(models.Model):
    _name = 'akpsi.product'
    _description = 'AKPSI Product'
    _inherit = 'mail.thread'
    _rec_name = 'product_name'

    product_name = fields.Char(string="Product Name", tracking=True)
    product_designer = fields.Many2one(comodel_name='res.partner', string="Designer", tracking=True)
    product_type = fields.Selection(string="Type", selection=[
        ('ppt','Power Point'),
        ('icon', 'Icon Bundle')
    ], tracking=True)
    product_doc = fields.Binary(string="Product", tracking=True)
    state = fields.Selection(string="Product State", selection=[
        ('draft','Draft'),
        ('submitted', 'Submitted'),
        ('validated', 'Validated'),
        ('accepted', 'Accepted'),
        ('back_to_draft', 'Back to Draft')
    ], default='draft', tracking=True)
    mp_ids = fields.One2many(comodel_name='marketplace', inverse_name='product_id', string='Markeplace')
    product_description = fields.Text(string="Description")
    product_tag = fields.Char(string="Hashtag")

    def action_submitted(self):
        for me in self:
            if me.state != 'draft':
                continue
            me.update({
                'state': 'submitted'
            })
        return

    def action_validated(self):
        for me in self:
            if me.state != 'submitted':
                continue
            me.update({
                'state': 'validated'
            })
        return

    def action_accepted(self):
        for me in self:
            if me.state != 'validated':
                continue
            me.update({
                'state': 'accepted'
            })
        return

    def action_back_to_draft(self):
        for me in self:
            if me.state != 'validated':
                continue
            me.update({
                'state': 'draft'
            })
        return

    def generate_tag(self):
        tags = {
            'art': {
                'hastag': "#Art #ArtistryUnveiled #BrushstrokesOfBeauty #PalettePassion #ArtisticExpressions",
                'desc': "Journey through Creativity: Unveiling the Canvas of Imagination. Exploring the Intersection of Passion and Expression in Every Brushstroke with this professional design"
            },
            'food': {
                'hastag': "#Food #FoodieFaves #DeliciousDelights #TastyTreats #FoodieAdventures #FlavorfulFiesta",
                'desc': "Dive into a visual feast of culinary excellence with our Food Exploration PowerPoint. This presentation is a delectable journey through the world of flavors, where each slide is a canvas showcasing the artistry of gastronomy. Join us as we celebrate the vibrant palette of global cuisines, explore innovative culinary trends, and share insights into the art and science of food. Bon appétit!"
            },
            'logistic': {
                'hastag': "#IconicLogistics #ShipAndDeliver #SupplyChainSymbols #TransportationIcons #WarehouseGraphics #LogisticsGlyphs",
                'desc': "Introducing our Logistics Icons Collection – a comprehensive set of meticulously designed symbols that seamlessly communicate the dynamics of supply chain management. Each icon encapsulates the essence of transportation, distribution, and seamless connectivity. Elevate your presentations, reports, or websites with these crisp, clear symbols that convey the precision and reliability inherent in every aspect of logistics. Navigate the world of logistics effortlessly with our intuitive and impactful iconography."
            },
            'furniture': {
                'hastag': "#FurnitureIcons #DesignElements #IconicInteriors #FurnishingsVisualized #StyleAndFunction #HomeInspiration #InteriorEssentials",
                'desc': "Discover the essence of style and functionality with our Furniture Icon Collection. Each icon is a visual testament to the artistry of interior design, meticulously crafted to represent a myriad of furnishings that transform spaces. Redefine visual storytelling in the world of interiors with our curated set of furniture icons."
            },
            'technology': {
                'hastag': "#TechInnovationsUnleashed #TechTrendsUnveiled #DigitalInnovationInsights #InnovateWithTech #DigitalRevolution",
                'desc': "Dive into the cutting-edge world of technology with our Technology Trends PowerPoint presentation. This dynamic and insightful presentation explores the latest innovations, emerging technologies, and their impact on industries. Join us in this technological journey, where ideas evolve, and possibilities are limitless. Equip yourself with knowledge that empowers innovation and drives progress."
            },
            'travel': {
                'hastag': "#TravelDreamsUnfold #WanderlustJourney #ExploreDreamDiscover #TravelTalesUnfold #AdventuresInSlides #DiscoverTheWorld",
                'desc': "Embark on a captivating journey around the globe with our Travel Adventure PowerPoint. This presentation is your passport to a world of wanderlust, featuring stunning visuals, insider tips, and immersive experiences. From iconic landmarks to hidden gems, each slide invites you to explore diverse cultures and landscapes. Whether you're a seasoned traveler or planning your first escapade, this presentation is your gateway to a world of discovery and adventure."
            },
            'business': {
                'hastag': "#BusinessInsights #CorporateStrategy #ExecutiveBriefing #MarketTrends #StrategicPlanning #BizPresentation",
                'desc': "Step into the realm of strategic innovation and business excellence with our Business Insights PowerPoint. Unlock the potential of your enterprise and chart a course towards strategic excellence with our Business Insights PowerPoint."
            },
            'medical': {
                'hastag': "#Medical #Health #HealthCare #HealthyLiving #MedicalInnovation",
                'desc': "Exploring Frontiers in Healthcare: Unveiling Innovations, Advancements, and a Commitment to Patient Well-being with this professional design"
            },
        }
        title = self.product_name
        words_in_title = title.lower().split()
        for me in self:
            for word in words_in_title:
                if word in tags:
                    me.update({
                        'product_description': tags[word]['desc'],
                        'product_tag': tags[word]['hastag']
                    })
        return


class Marketplace(models.Model):
    _name = 'marketplace'
    _description = 'Marketplace'
    _inherit = 'mail.thread'
    _rec_name = 'mp_name'

    mp_name = fields.Selection(string="Marketplace Name", selection=[
        ('graphicriver', 'Graphicriver'),
        ('envato_elements', 'Envato Elements'),
        ('canva', 'Canva'),
        ('iconfinder','Iconfinder'),
        ('iconscout', 'Iconscout'),
        ('adobe_stock', 'Adobe Stock'),
        ('thenounproject', 'Thenounproject')
    ])
    mp_sku = fields.Char(string="SKU")
    product_id = fields.Many2one(comodel_name='akpsi.product', string="Product")
    product_description = fields.Text(string="Description")
    product_tag = fields.Char(string="Hashtag")
