from flask import Flask, request, abort
from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.webhooks import (
    MessageEvent,
    FollowEvent,
    PostbackEvent,
    TextMessageContent
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    MessagingApiBlob,
    ReplyMessageRequest,
    TextMessage,
    StickerMessage,
    ImageMessage,
    VideoMessage,
    AudioMessage,
    LocationMessage,
    ImagemapMessage,
    ImagemapArea,
    ImagemapBaseSize,
    ImagemapExternalLink,
    ImagemapVideo,
    URIImagemapAction,
    MessageImagemapAction,
    FlexMessage,
    FlexContainer,
    TemplateMessage,
    ConfirmTemplate,
    ButtonsTemplate,
    CarouselTemplate,
    ImageCarouselTemplate,
    MessageAction,
    URIAction,
    PostbackAction,
    DatetimePickerAction,
    CameraAction,
    CameraRollAction,
    LocationAction,
    CarouselColumn,
    ImageCarouselColumn,
    QuickReply,
    QuickReplyItem,
    RichMenuRequest,
    CreateRichMenuAliasRequest
)
import line_flex
import os

app = Flask(__name__)

CHANNEL_ACCESS_TOKEN = os.getenv("CHANNEL_ACCESS_TOKEN")
CHANNEL_SECRET = os.getenv("CHANNEL_SECRET")
    
line_handler = WebhookHandler(CHANNEL_SECRET)
configuration = Configuration(access_token=CHANNEL_ACCESS_TOKEN)

@app.route("/")
def index():
    return "202412 LINE Bot Workshop"

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        line_handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@line_handler.add(MessageEvent, message=TextMessageContent)
def handle_messsage(event):
    message = event.message.text
    url_root = request.url_root.replace("http:", "https:")
    if message == "主選單":
        flex_json = line_flex.main_line_flex_str()
        reply_message(event, [FlexMessage(alt_text=message, contents=FlexContainer.from_json(flex_json))])
    elif message == "Action Types":
        flex_json = line_flex.actions_line_flex_str()
        reply_message(event, [FlexMessage(alt_text=message, contents=FlexContainer.from_json(flex_json))])
    elif message == "Message Types":
        flex_json = line_flex.messages_line_flex_str()
        reply_message(event, [FlexMessage(alt_text=message, contents=FlexContainer.from_json(flex_json))])
    elif message == "Template message":
        flex_json = line_flex.template_line_flex_str()
        reply_message(event, [FlexMessage(alt_text=message, contents=FlexContainer.from_json(flex_json))])
    elif message == "Flex message":
        flex_json = line_flex.flex_line_flex_str()
        reply_message(event, [FlexMessage(alt_text=message, contents=FlexContainer.from_json(flex_json))])
    elif message == "Text message":
        reply_message(event, [TextMessage(text="Text message")])
    elif message == "Sticker message":
        reply_message(event, [StickerMessage(package_id="446", sticker_id="1988")])
    elif message == "Image message":
        url = f"{url_root}static/logo.png"
        reply_message(event, [ImageMessage(original_content_url=url, preview_image_url=url)])
    elif message == "Video message":
        url = f"{url_root}static/video.mp4"
        reply_message(event, [VideoMessage(original_content_url=url, preview_image_url=url)])
    elif message == "Audio message":
        url = f"{url_root}static/music.mp3"
        reply_message(event, [AudioMessage(original_content_url=url, duration=60000)])
    elif message == "Location message":
        reply_message(event, [LocationMessage(title='Location', address="Taipei", latitude=25.0475, longitude=121.5173)])
    elif message == "Imagemap message":
        reply_message(event, [                    
            ImagemapMessage(
                base_url=f"{url_root}static/imagemap",
                alt_text='this is an imagemap',
                base_size=ImagemapBaseSize(height=1040, width=1040),
                video=ImagemapVideo(
                    original_content_url=f"{url_root}static/video.mp4",
                    preview_image_url=f"{url_root}static/preview_image.png",
                    area=ImagemapArea(
                        x=0, y=0, width=1040, height=520
                    ),
                    external_link=ImagemapExternalLink(
                        link_uri='https://www.youtube.com/@bigdatantue',
                        label='點我看更多',
                    ),
                ),
                actions=[
                    URIImagemapAction(
                        type = "uri",
                        linkUri='https://instagram.com/ntue.bigdata?igshid=YmMyMTA2M2Y=',
                        area=ImagemapArea(
                            x=0, y=520, width=520, height=520
                        )
                    ),
                    MessageImagemapAction(
                        type ="message",
                        text='這是fb網頁https://www.facebook.com/NTUEBIGDATAEDU',
                        area=ImagemapArea(
                            x=520, y=520, width=520, height=520
                        )
                    )
                ]
            )
        ])
    elif message == "Confirm Template":
        confirm_template = ConfirmTemplate(
            text='訂閱追蹤國北教大教育大數據了嗎?',
            actions=[
                MessageAction(label='是', text='是!'),
                MessageAction(label='否', text='否!')
            ]
        )
        reply_message(event, [TemplateMessage(alt_text='Confirm Template', template=confirm_template)])
    elif message == "Button Template":
        buttons_template = ButtonsTemplate(
                thumbnail_image_url= f"{url_root}static/Logo.png",
                title='相關社群連結',
                text='教育大數據的社群連結',
                actions=[
                    URIAction(label='教育大數據微學程FB連結', uri='https://www.facebook.com/NTUEBIGDATAEDU'),
                    URIAction(label='教育大數據微學程YT連結', uri='https://www.youtube.com/@bigdatantue'),
                    URIAction(label='教育大數據微學程IG連結', uri='https://www.instagram.com/ntue.bigdata')
                ]
            )
        reply_message(event, [TemplateMessage(alt_text="Buttom Template", template=buttons_template)])
    elif message == "Carousel Template":
        carousel_template = CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url=f"{url_root}static/FB.png",
                    title='Facebook',
                    text='大數據教育微學程FB粉絲專頁',
                    actions=[
                        URIAction(
                            label='按我前往Facebook',
                            uri='https://www.facebook.com/NTUEBIGDATAEDU'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=f"{url_root}static/YT.png",
                    title='Youtube',
                    text='大數據教育微學程Youtube頻道',
                    actions=[
                        URIAction(
                            label='按我前往Youtube',
                            uri='https://www.youtube.com/@bigdatantue'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=f"{url_root}static/IG.png",
                    title='Instagram',
                    text='大數據教育微學程Instagram帳號',
                    actions=[
                        URIAction(
                            label='按我前往 Instagram',
                            uri='https://www.instagram.com/ntue.bigdata'
                        )
                    ]
                )
            ]
        )
        reply_message(event, [TemplateMessage(alt_text='Carousel Template', template=carousel_template)])
    elif message == "Image Carousel Template":
        image_carousel_template = ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url=f"{url_root}static/facebook.png",
                    action=URIAction(
                        label='造訪FB',
                        uri='https://www.facebook.com/NTUEBIGDATAEDU'
                    )
                ),
                ImageCarouselColumn(
                    image_url=f"{url_root}static/youtube.png",
                    action=URIAction(
                        label='造訪YT',
                        uri='https://www.youtube.com/@bigdatantue'
                    )
                ),
                ImageCarouselColumn(
                    image_url=f"{url_root}static/instagram.png",
                    action=URIAction(
                        label='造訪IG',
                        uri='https://www.instagram.com/ntue.bigdata'
                    )
                )                
            ]
        )
        reply_message(event, [TemplateMessage(alt_text='Image Carousel Template', template=image_carousel_template)])
    elif message == "Line Flex Message" or message == "Schedule":
        flex_json = line_flex.scedule_line_flex_str()
        reply_message(event, [FlexMessage(alt_text=message, contents=FlexContainer.from_json(flex_json))])
    elif message == "Quick Reply":
        quick_reply = TextMessage(
            text='請選擇項目',
            quick_reply=QuickReply(
                items=[
                    QuickReplyItem(
                        action=PostbackAction(
                            label="Postback",
                            data="Postback"
                        )
                    ),
                    QuickReplyItem(
                        action=MessageAction(
                            label="Message",
                            text="message"
                        )
                    ),
                    QuickReplyItem(
                        action=URIAction(
                            label="URI",
                            uri="https://www.instagram.com/ntue.bigdata"
                        )
                    ),
                    QuickReplyItem(
                        action=DatetimePickerAction(
                            label="Datetime Picker",
                            data="Datetimepicker",
                            mode="datetime"
                        )
                    ),
                    QuickReplyItem(
                        action=CameraAction(label="Camera")
                    ),
                    QuickReplyItem(
                        action=CameraRollAction(label="Camera Roll")
                    ),
                    QuickReplyItem(
                        action=LocationAction(label="Location")
                    )
                ]
            )
        )
        reply_message(event, [quick_reply])
    else:
        reply_message(event, [TextMessage(text=message)])

@line_handler.add(FollowEvent)
def handle_follow(event):
    reply_message(event, [TextMessage(text="歡迎加入我們的工作坊Line Bot")])
    
@line_handler.add(PostbackEvent)
def handle_postback(event):
    postback_data = event.postback.data
    if postback_data == "Postback":
        raw_body = request.get_data(as_text=True)
        reply_message(event, [TextMessage(text=raw_body)])
    elif postback_data == "Datetimepicker":
        datetime = event.postback.params['datetime']
        raw_body = request.get_data(as_text=True)
        reply_message(event, [TextMessage(text=datetime), TextMessage(text=raw_body)])
    else:
        reply_message(event, [TextMessage(text=event.postback.data)])

def reply_message(event, messages):
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=messages
            )
        )

# 設定rich menu(只需執行一次)
def init_rich_menu():
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        line_bot_blob_api = MessagingApiBlob(api_client)
        # ============================== 創建圖文選單a ==============================
        rich_menu_a_str = """{
            "size": {
                "width": 2500,
                "height": 1686
            },
            "selected": true,
            "name": "圖文選單 1",
            "chatBarText": "查看更多資訊",
            "areas": [
                {
                "bounds": {
                    "x": 1359,
                    "y": 0,
                    "width": 1141,
                    "height": 253
                },
                "action": { 
                    "type": "richmenuswitch", 
                    "richMenuAliasId": "richmenu_b", 
                    "data": "richmenu-changed-to-b"
                }
                },
                {
                "bounds": {
                    "x": 226,
                    "y": 494,
                    "width": 903,
                    "height": 356
                },
                "action": {
                    "type": "message",
                    "text": "Schedule"
                }
                },
                {
                "bounds": {
                    "x": 1365,
                    "y": 491,
                    "width": 903,
                    "height": 356
                },
                "action": {
                    "type": "uri",
                    "uri": "https://hackmd.io/@RPmo8A9DR_-YHXZSO6fyzA/Syqem4Lfkx"
                }
                },
                {
                "bounds": {
                    "x": 226,
                    "y": 997,
                    "width": 903,
                    "height": 353
                },
                "action": {
                    "type": "uri",
                    "uri": "https://forms.gle/PjNZDAQCZUzs9JTM6"
                }
                },
                {
                "bounds": {
                    "x": 1362,
                    "y": 991,
                    "width": 903,
                    "height": 356
                },
                "action": {
                    "type": "uri",
                    "uri": "https://linktr.ee/ntue.bigdata"
                }
                }
            ]
        }"""

        rich_menu_a_id = line_bot_api.create_rich_menu(
            rich_menu_request=RichMenuRequest.from_json(rich_menu_a_str)
        ).rich_menu_id

        with open('./static/richmenu1.png', 'rb') as image:
            line_bot_blob_api.set_rich_menu_image(
                rich_menu_id=rich_menu_a_id,
                body=bytearray(image.read()),
                _headers={'Content-Type': 'image/png'}
            )

        line_bot_api.set_default_rich_menu(rich_menu_a_id)

        line_bot_api.create_rich_menu_alias(
            CreateRichMenuAliasRequest(
                rich_menu_alias_id="richmenu_a",
                rich_menu_id=rich_menu_a_id
            )
        )

        # ============================== 創建圖文選單b ==============================
        rich_menu_b_str = """{
            "size": {
                "width": 2500,
                "height": 1686
            },
            "selected": true,
            "name": "圖文選單 2",
            "chatBarText": "查看更多資訊",
            "areas": [
            {
                "bounds": {
                    "x": 0,
                    "y": 0,
                    "width": 1162,
                    "height": 259
                },
                "action": { 
                    "type": "richmenuswitch", 
                    "richMenuAliasId": "richmenu_a", 
                    "data": "richmenu-changed-to-a"
                }
            },
            {
                "bounds": {
                    "x": 324,
                    "y": 476,
                    "width": 685,
                    "height": 462
                },
                "action": {
                    "type": "message",
                    "text": "Message Types"
                }
            },
            {
                "bounds": {
                    "x": 1262,
                    "y": 447,
                    "width": 714,
                    "height": 471
                },
                "action": {
                    "type": "message",
                    "text": "Action Types"
                }
            },
            {
                "bounds": {
                    "x": 750,
                    "y": 1026,
                    "width": 694,
                    "height": 450
                },
                "action": {
                    "type": "message",
                    "text": "Quick Reply"
                }
            }
            ]
        }"""

        rich_menu_b_id = line_bot_api.create_rich_menu(
            rich_menu_request=RichMenuRequest.from_json(rich_menu_b_str)
        ).rich_menu_id

        with open('./static/richmenu2.png', 'rb') as image:
            line_bot_blob_api.set_rich_menu_image(
                rich_menu_id=rich_menu_b_id,
                body=bytearray(image.read()),
                _headers={'Content-Type': 'image/png'}
            )

        line_bot_api.create_rich_menu_alias(
            CreateRichMenuAliasRequest(
                rich_menu_alias_id="richmenu_b",
                rich_menu_id=rich_menu_b_id
            )
        )
        
# init_rich_menu()

# 查詢rich menu
# with ApiClient(configuration) as api_client:
#     line_bot_api = MessagingApi(api_client)
#     richmenulist = line_bot_api.get_rich_menu_list()

# for rich_menu in richmenulist.richmenus:
#     print(rich_menu.rich_menu_id)

# 刪除所有rich menu
# with ApiClient(configuration) as api_client:
#     line_bot_api = MessagingApi(api_client)
#     richmenulist = line_bot_api.get_rich_menu_alias_list()

# for rich_menu in richmenulist.aliases:
#     line_bot_api.delete_rich_menu(rich_menu.rich_menu_id)
#     line_bot_api.delete_rich_menu_alias(rich_menu.rich_menu_alias_id)

if __name__ == "__main__":
    app.run()