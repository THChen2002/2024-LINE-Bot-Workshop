def main_line_flex_str():
    return """{
        "type": "bubble",
        "header": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "text",
                "text": "LINE Bot開發實戰工作坊",
                "color": "#ffffff",
                "align": "center"
            }
            ],
            "backgroundColor": "#367def"
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "功能展示",
                    "size": "xl",
                    "weight": "bold",
                    "align": "center"
                }
                ]
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "button",
                    "style": "primary",
                    "height": "sm",
                    "action": {
                    "type": "message",
                    "label": "Message Types",
                    "text": "Message Types"
                    },
                    "color": "#0066CC"
                },
                {
                    "type": "button",
                    "style": "primary",
                    "height": "sm",
                    "action": {
                    "type": "message",
                    "label": "Action Types",
                    "text": "Action Types"
                    },
                    "color": "#367def",
                    "margin": "sm"
                },
                {
                    "type": "button",
                    "style": "primary",
                    "height": "sm",
                    "action": {
                    "type": "message",
                    "label": "Quick Reply",
                    "text": "Quick Reply"
                    },
                    "color": "#66B3FF",
                    "margin": "sm"
                }
                ],
                "margin": "md"
            }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "text",
                "text": "國北教大教育大數據微學程",
                "align": "center",
                "size": "xs"
            }
            ],
            "backgroundColor": "#f9fafc"
        }
    }"""
    
def messages_line_flex_str():
    return """{
        "type": "bubble",
        "header": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "text",
                "text": "LINE Bot開發實戰工作坊",
                "color": "#ffffff",
                "align": "center"
            }
            ],
            "backgroundColor": "#367def"
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "Message Types Demo",
                    "wrap": true,
                    "weight": "bold",
                    "align": "center",
                    "color": "#404f6d",
                    "size": "xl"
                }
                ]
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "button",
                    "style": "primary",
                    "height": "sm",
                    "action": {
                    "type": "message",
                    "label": "Text message",
                    "text": "Text message"
                    },
                    "color": "#00aeff"
                },
                {
                    "type": "button",
                    "style": "primary",
                    "height": "sm",
                    "action": {
                    "type": "message",
                    "label": "Sticker message",
                    "text": "Sticker message"
                    },
                    "color": "#3369e7",
                    "margin": "sm"
                },
                {
                    "type": "button",
                    "style": "primary",
                    "height": "sm",
                    "action": {
                    "type": "message",
                    "label": "Image message",
                    "text": "Image message"
                    },
                    "color": "#8e43e7",
                    "margin": "sm"
                },
                {
                    "type": "button",
                    "style": "primary",
                    "height": "sm",
                    "action": {
                    "type": "message",
                    "label": "Video message",
                    "text": "Video message"
                    },
                    "color": "#b84592",
                    "margin": "sm"
                },
                {
                    "type": "button",
                    "style": "primary",
                    "height": "sm",
                    "action": {
                    "type": "message",
                    "label": "Audio message",
                    "text": "Audio message"
                    },
                    "color": "#ff4f81",
                    "margin": "sm"
                },
                {
                    "type": "button",
                    "style": "primary",
                    "height": "sm",
                    "action": {
                    "type": "message",
                    "label": "Location message",
                    "text": "Location message"
                    },
                    "color": "#ff6c5f",
                    "margin": "sm"
                },
                {
                    "type": "button",
                    "style": "primary",
                    "height": "sm",
                    "action": {
                    "type": "message",
                    "label": "Imagemap message",
                    "text": "Imagemap message"
                    },
                    "color": "#ffc168",
                    "margin": "sm"
                },
                {
                    "type": "button",
                    "style": "primary",
                    "height": "sm",
                    "action": {
                    "type": "message",
                    "label": "Template message",
                    "text": "Template message"
                    },
                    "color": "#00c16e",
                    "margin": "sm"
                },
                {
                    "type": "button",
                    "style": "primary",
                    "height": "sm",
                    "action": {
                    "type": "message",
                    "label": "Flex message",
                    "text": "Flex message"
                    },
                    "color": "#1cc7d0",
                    "margin": "sm"
                }
                ],
                "margin": "md"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "button",
                    "style": "secondary",
                    "height": "sm",
                    "action": {
                    "type": "message",
                    "label": "回主選單",
                    "text": "主選單"
                    },
                    "color": "#ECF5FF"
                }
                ],
                "margin": "md"
            }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "text",
                "text": "國北教大教育大數據微學程",
                "align": "center",
                "size": "xs"
            }
            ],
            "backgroundColor": "#f9fafc"
        },
        "styles": {
            "hero": {
            "backgroundColor": "#367def"
            }
        }
    }"""
        
def template_line_flex_str():
    return """{
        "type": "bubble",
        "header": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "text",
                "text": "LINE Bot開發實戰工作坊",
                "color": "#ffffff",
                "align": "center"
            }
            ],
            "backgroundColor": "#367def"
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "Template Message",
                    "align": "center",
                    "weight": "bold",
                    "size": "xl"
                }
                ]
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "想要簡單快速地呈現你的資料嗎？",
                    "wrap": true,
                    "weight": "bold",
                    "align": "start",
                    "color": "#404f6d",
                    "margin": "md"
                },
                {
                    "type": "text",
                    "text": "快來看系統提供了哪些內建卡片吧！",
                    "wrap": true,
                    "weight": "bold",
                    "align": "start",
                    "color": "#404f6d"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "button",
                        "style": "primary",
                        "height": "sm",
                        "action": {
                        "type": "message",
                        "label": "Confirm Template",
                        "text": "Confirm Template"
                        },
                        "color": "#0066CC"
                    },
                    {
                        "type": "button",
                        "style": "primary",
                        "height": "sm",
                        "action": {
                        "type": "message",
                        "label": "Button Template",
                        "text": "Button Template"
                        },
                        "color": "#367def",
                        "margin": "sm"
                    },
                    {
                        "type": "button",
                        "style": "primary",
                        "height": "sm",
                        "action": {
                        "type": "message",
                        "label": "Carousel Template",
                        "text": "Carousel Template"
                        },
                        "color": "#66B3FF",
                        "margin": "sm"
                    },
                    {
                        "type": "button",
                        "style": "primary",
                        "height": "sm",
                        "action": {
                        "type": "message",
                        "label": "Image Carousel Template",
                        "text": "Image Carousel Template"
                        },
                        "color": "#84C1FF",
                        "margin": "sm"
                    }
                    ],
                    "margin": "md"
                }
                ]
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "button",
                    "style": "secondary",
                    "height": "sm",
                    "action": {
                    "type": "message",
                    "label": "回主選單",
                    "text": "主選單"
                    },
                    "color": "#ECF5FF"
                }
                ],
                "margin": "md"
            }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "text",
                "text": "國北教大教育大數據微學程",
                "align": "center",
                "size": "xs"
            }
            ],
            "backgroundColor": "#f9fafc"
        }
    }"""
    
def actions_line_flex_str():
    return """{
        "type": "bubble",
        "header": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "text",
                "text": "LINE Bot開發實戰工作坊",
                "color": "#ffffff",
                "align": "center"
            }
            ],
            "backgroundColor": "#367def"
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "Button Actions Demo",
                    "wrap": true,
                    "weight": "bold",
                    "align": "center",
                    "color": "#404f6d",
                    "size": "xl"
                }
                ]
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "button",
                    "style": "primary",
                    "action": {
                    "type": "message",
                    "label": "Message",
                    "text": "Message"
                    },
                    "color": "#367def",
                    "height": "sm"
                },
                {
                    "type": "button",
                    "style": "primary",
                    "height": "sm",
                    "action": {
                    "type": "postback",
                    "label": "Postback",
                    "data": "Postback"
                    },
                    "color": "#01B468",
                    "margin": "sm"
                },
                {
                    "type": "button",
                    "style": "primary",
                    "height": "sm",
                    "action": {
                    "type": "uri",
                    "label": "URI",
                    "uri": "https://linktr.ee/ntue.bigdata"
                    },
                    "color": "#FF359A",
                    "margin": "sm"
                },
                {
                    "type": "button",
                    "style": "primary",
                    "height": "sm",
                    "action": {
                    "type": "datetimepicker",
                    "data": "Datetimepicker",
                    "mode": "datetime",
                    "label": "Datetime picker"
                    },
                    "color": "#B15BFF",
                    "margin": "sm"
                }
                ],
                "margin": "md"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "button",
                    "style": "secondary",
                    "height": "sm",
                    "action": {
                    "type": "message",
                    "label": "回主選單",
                    "text": "主選單"
                    },
                    "color": "#ECF5FF"
                }
                ],
                "margin": "md"
            }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "text",
                "text": "國北教大教育大數據微學程",
                "align": "center",
                "size": "xs"
            }
            ],
            "backgroundColor": "#f9fafc"
        },
        "styles": {
            "hero": {
            "backgroundColor": "#367def"
            }
        }
    }"""
    
def flex_line_flex_str():
    return """{
        "type": "bubble",
        "header": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "text",
                "text": "LINE Bot開發實戰工作坊",
                "color": "#ffffff",
                "align": "center"
            }
            ],
            "backgroundColor": "#367def"
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "Flex Message",
                    "size": "xl",
                    "align": "center",
                    "weight": "bold"
                }
                ]
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "想製作卡片卻不知如何下手嗎？有了Line Flex Message就能讓你輕鬆做出屬於你的獨特卡片喔！",
                    "wrap": true,
                    "weight": "bold",
                    "align": "start",
                    "color": "#404f6d"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "button",
                        "style": "primary",
                        "height": "sm",
                        "action": {
                        "type": "message",
                        "label": "Line Flex Message",
                        "text": "Line Flex Message"
                        },
                        "color": "#367def"
                    },
                    {
                        "type": "button",
                        "style": "primary",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "Line Flex Simulator",
                        "uri": "https://developers.line.biz/flex-simulator/"
                        },
                        "color": "#66B3FF",
                        "margin": "sm"
                    }
                    ],
                    "margin": "md"
                }
                ],
                "margin": "md"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "button",
                    "style": "secondary",
                    "height": "sm",
                    "action": {
                    "type": "message",
                    "label": "回主選單",
                    "text": "主選單"
                    },
                    "color": "#ECF5FF"
                }
                ],
                "margin": "md"
            }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "text",
                "text": "國北教大教育大數據微學程",
                "align": "center",
                "size": "xs"
            }
            ],
            "backgroundColor": "#f9fafc"
        }
    }"""

def scedule_line_flex_str():
    return """{
        "type": "carousel",
        "contents": [
            {
            "type": "bubble",
            "size": "mega",
            "header": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "Dec. 28, 2024",
                        "color": "#ffffff",
                        "size": "sm"
                    }
                    ],
                    "position": "absolute",
                    "offsetStart": "200px",
                    "offsetTop": "15px"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "FROM",
                        "color": "#ffffff66",
                        "size": "sm"
                    },
                    {
                        "type": "text",
                        "text": "Anywhere",
                        "color": "#ffffff",
                        "size": "xl",
                        "flex": 4,
                        "weight": "bold"
                    }
                    ]
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "TO",
                        "color": "#ffffff66",
                        "size": "sm"
                    },
                    {
                        "type": "text",
                        "text": "NTUE F401b",
                        "color": "#ffffff",
                        "size": "xl",
                        "flex": 4,
                        "weight": "bold"
                    }
                    ]
                }
                ],
                "paddingAll": "20px",
                "backgroundColor": "#004B97",
                "spacing": "md",
                "height": "154px",
                "paddingTop": "22px"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "Total: 6 hours",
                    "color": "#b7b7b7",
                    "size": "xs"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "text",
                        "text": "09:00",
                        "size": "sm",
                        "gravity": "center",
                        "align": "end"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "filler"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [],
                            "cornerRadius": "30px",
                            "height": "12px",
                            "width": "12px",
                            "borderColor": "#EF454D",
                            "borderWidth": "2px"
                        },
                        {
                            "type": "filler"
                        }
                        ],
                        "flex": 0
                    },
                    {
                        "type": "text",
                        "text": "Start",
                        "gravity": "center",
                        "flex": 4,
                        "size": "sm"
                    }
                    ],
                    "spacing": "lg",
                    "cornerRadius": "30px",
                    "margin": "xl"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "text",
                            "text": "3hr",
                            "gravity": "center",
                            "size": "xs",
                            "color": "#8c8c8c",
                            "align": "end"
                        }
                        ],
                        "flex": 1
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "filler"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [],
                                "width": "2px",
                                "backgroundColor": "#6486E3"
                            },
                            {
                                "type": "filler"
                            }
                            ],
                            "flex": 1
                        }
                        ],
                        "width": "12px"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "LINE Bot Basic",
                            "gravity": "center",
                            "size": "xs",
                            "color": "#8c8c8c"
                        },
                        {
                            "type": "text",
                            "text": "LINE Official Account",
                            "gravity": "center",
                            "size": "xs",
                            "color": "#8c8c8c",
                            "wrap": true
                        }
                        ],
                        "flex": 4,
                        "justifyContent": "center"
                    }
                    ],
                    "spacing": "lg",
                    "height": "72px"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "text",
                            "text": "12:00",
                            "gravity": "center",
                            "size": "sm",
                            "align": "end"
                        }
                        ],
                        "flex": 1
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "filler"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [],
                            "cornerRadius": "30px",
                            "width": "12px",
                            "height": "12px",
                            "borderWidth": "2px",
                            "borderColor": "#6486E3"
                        },
                        {
                            "type": "filler"
                        }
                        ],
                        "flex": 0
                    },
                    {
                        "type": "text",
                        "text": "Break",
                        "gravity": "center",
                        "flex": 4,
                        "size": "sm"
                    }
                    ],
                    "spacing": "lg",
                    "cornerRadius": "30px"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "text",
                            "text": "1hr",
                            "gravity": "center",
                            "size": "xs",
                            "color": "#8c8c8c",
                            "align": "end"
                        }
                        ],
                        "flex": 1
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "filler"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [],
                                "width": "2px",
                                "backgroundColor": "#B7B7B7"
                            },
                            {
                                "type": "filler"
                            }
                            ],
                            "flex": 1
                        }
                        ],
                        "width": "12px"
                    },
                    {
                        "type": "text",
                        "text": "Lunch",
                        "gravity": "center",
                        "flex": 4,
                        "size": "xs",
                        "color": "#8c8c8c"
                    }
                    ],
                    "spacing": "lg",
                    "height": "24px"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "text",
                        "text": "13:00",
                        "gravity": "center",
                        "size": "sm",
                        "align": "end"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "filler"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [],
                            "cornerRadius": "30px",
                            "width": "12px",
                            "height": "12px",
                            "borderColor": "#EF454D",
                            "borderWidth": "2px"
                        },
                        {
                            "type": "filler"
                        }
                        ],
                        "flex": 0
                    },
                    {
                        "type": "text",
                        "text": "Continue",
                        "gravity": "center",
                        "flex": 4,
                        "size": "sm"
                    }
                    ],
                    "spacing": "lg",
                    "cornerRadius": "30px"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "text",
                            "text": "3hr",
                            "gravity": "center",
                            "size": "xs",
                            "color": "#8c8c8c",
                            "align": "end"
                        }
                        ],
                        "flex": 1
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "filler"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [],
                                "width": "2px",
                                "backgroundColor": "#6486E3"
                            },
                            {
                                "type": "filler"
                            }
                            ],
                            "flex": 1
                        }
                        ],
                        "width": "12px"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "Development Environment Introduction",
                            "gravity": "center",
                            "size": "xs",
                            "color": "#8c8c8c",
                            "wrap": true
                        },
                        {
                            "type": "text",
                            "text": "Echo Bot",
                            "gravity": "center",
                            "size": "xs",
                            "color": "#8c8c8c"
                        }
                        ],
                        "flex": 4,
                        "justifyContent": "center"
                    }
                    ],
                    "spacing": "lg",
                    "height": "72px"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "text",
                        "text": "16:00",
                        "gravity": "center",
                        "size": "sm",
                        "align": "end"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "filler"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [],
                            "cornerRadius": "30px",
                            "width": "12px",
                            "height": "12px",
                            "borderColor": "#6486E3",
                            "borderWidth": "2px"
                        },
                        {
                            "type": "filler"
                        }
                        ],
                        "flex": 0
                    },
                    {
                        "type": "text",
                        "text": "Happy Ending",
                        "gravity": "center",
                        "flex": 4,
                        "size": "sm"
                    }
                    ],
                    "spacing": "lg",
                    "cornerRadius": "30px"
                }
                ]
            }
            },
            {
            "type": "bubble",
            "size": "mega",
            "header": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "Dec. 29, 2024",
                        "color": "#ffffff",
                        "size": "sm"
                    }
                    ],
                    "position": "absolute",
                    "offsetStart": "200px",
                    "offsetTop": "15px"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "FROM",
                        "color": "#ffffff66",
                        "size": "sm"
                    },
                    {
                        "type": "text",
                        "text": "Anywhere",
                        "color": "#ffffff",
                        "size": "xl",
                        "flex": 4,
                        "weight": "bold"
                    }
                    ]
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "TO",
                        "color": "#ffffff66",
                        "size": "sm"
                    },
                    {
                        "type": "text",
                        "text": "NTUE F401b",
                        "color": "#ffffff",
                        "size": "xl",
                        "flex": 4,
                        "weight": "bold"
                    }
                    ]
                }
                ],
                "paddingAll": "20px",
                "backgroundColor": "#004B97",
                "spacing": "md",
                "height": "154px",
                "paddingTop": "22px"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "Total: 6 hours",
                    "color": "#b7b7b7",
                    "size": "xs"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "text",
                        "text": "09:00",
                        "size": "sm",
                        "gravity": "center",
                        "align": "end"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "filler"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [],
                            "cornerRadius": "30px",
                            "height": "12px",
                            "width": "12px",
                            "borderColor": "#EF454D",
                            "borderWidth": "2px"
                        },
                        {
                            "type": "filler"
                        }
                        ],
                        "flex": 0
                    },
                    {
                        "type": "text",
                        "text": "Start",
                        "gravity": "center",
                        "flex": 4,
                        "size": "sm"
                    }
                    ],
                    "spacing": "lg",
                    "cornerRadius": "30px",
                    "margin": "xl"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "text",
                            "text": "3hr",
                            "gravity": "center",
                            "size": "xs",
                            "color": "#8c8c8c",
                            "align": "end"
                        }
                        ],
                        "flex": 1
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "filler"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [],
                                "width": "2px",
                                "backgroundColor": "#6486E3"
                            },
                            {
                                "type": "filler"
                            }
                            ],
                            "flex": 1
                        }
                        ],
                        "width": "12px"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "Messaging API",
                            "gravity": "center",
                            "size": "xs",
                            "color": "#8c8c8c"
                        },
                        {
                            "type": "text",
                            "text": "LINE Bot Application",
                            "gravity": "center",
                            "size": "xs",
                            "color": "#8c8c8c"
                        }
                        ],
                        "flex": 4,
                        "justifyContent": "center"
                    }
                    ],
                    "spacing": "lg",
                    "height": "72px"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "text",
                            "text": "12:00",
                            "gravity": "center",
                            "size": "sm",
                            "align": "end"
                        }
                        ],
                        "flex": 1
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "filler"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [],
                            "cornerRadius": "30px",
                            "width": "12px",
                            "height": "12px",
                            "borderWidth": "2px",
                            "borderColor": "#6486E3"
                        },
                        {
                            "type": "filler"
                        }
                        ],
                        "flex": 0
                    },
                    {
                        "type": "text",
                        "text": "Break",
                        "gravity": "center",
                        "flex": 4,
                        "size": "sm"
                    }
                    ],
                    "spacing": "lg",
                    "cornerRadius": "30px"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "text",
                            "text": "1hr",
                            "gravity": "center",
                            "size": "xs",
                            "color": "#8c8c8c",
                            "align": "end"
                        }
                        ],
                        "flex": 1
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "filler"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [],
                                "width": "2px",
                                "backgroundColor": "#B7B7B7"
                            },
                            {
                                "type": "filler"
                            }
                            ],
                            "flex": 1
                        }
                        ],
                        "width": "12px"
                    },
                    {
                        "type": "text",
                        "text": "Lunch",
                        "gravity": "center",
                        "flex": 4,
                        "size": "xs",
                        "color": "#8c8c8c"
                    }
                    ],
                    "spacing": "lg",
                    "height": "24px"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "text",
                        "text": "13:00",
                        "gravity": "center",
                        "size": "sm",
                        "align": "end"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "filler"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [],
                            "cornerRadius": "30px",
                            "width": "12px",
                            "height": "12px",
                            "borderColor": "#EF454D",
                            "borderWidth": "2px"
                        },
                        {
                            "type": "filler"
                        }
                        ],
                        "flex": 0
                    },
                    {
                        "type": "text",
                        "text": "Continue",
                        "gravity": "center",
                        "flex": 4,
                        "size": "sm"
                    }
                    ],
                    "spacing": "lg",
                    "cornerRadius": "30px"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "text",
                            "text": "3hr",
                            "gravity": "center",
                            "size": "xs",
                            "color": "#8c8c8c",
                            "align": "end"
                        }
                        ],
                        "flex": 1
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "filler"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [],
                                "width": "2px",
                                "backgroundColor": "#6486E3"
                            },
                            {
                                "type": "filler"
                            }
                            ],
                            "flex": 1
                        }
                        ],
                        "width": "12px"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "Spreadsheet API",
                            "gravity": "center",
                            "size": "xs",
                            "color": "#8c8c8c"
                        },
                        {
                            "type": "text",
                            "text": "Firebase API",
                            "gravity": "center",
                            "size": "xs",
                            "color": "#8c8c8c"
                        }
                        ],
                        "flex": 4,
                        "justifyContent": "center"
                    }
                    ],
                    "spacing": "lg",
                    "height": "72px"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "text",
                        "text": "16:00",
                        "gravity": "center",
                        "size": "sm",
                        "align": "end"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "filler"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [],
                            "cornerRadius": "30px",
                            "width": "12px",
                            "height": "12px",
                            "borderColor": "#6486E3",
                            "borderWidth": "2px"
                        },
                        {
                            "type": "filler"
                        }
                        ],
                        "flex": 0
                    },
                    {
                        "type": "text",
                        "text": "Happy Ending",
                        "gravity": "center",
                        "flex": 4,
                        "size": "sm"
                    }
                    ],
                    "spacing": "lg",
                    "cornerRadius": "30px"
                }
                ]
            }
            },
            {
            "type": "bubble",
            "size": "mega",
            "header": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "Jan. 4, 2025",
                        "color": "#ffffff",
                        "size": "sm"
                    }
                    ],
                    "position": "absolute",
                    "offsetStart": "200px",
                    "offsetTop": "15px"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "FROM",
                        "color": "#ffffff66",
                        "size": "sm"
                    },
                    {
                        "type": "text",
                        "text": "Anywhere",
                        "color": "#ffffff",
                        "size": "xl",
                        "flex": 4,
                        "weight": "bold"
                    }
                    ]
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "TO",
                        "color": "#ffffff66",
                        "size": "sm"
                    },
                    {
                        "type": "text",
                        "text": "NTUE F401b",
                        "color": "#ffffff",
                        "size": "xl",
                        "flex": 4,
                        "weight": "bold"
                    }
                    ]
                }
                ],
                "paddingAll": "20px",
                "backgroundColor": "#004B97",
                "spacing": "md",
                "height": "154px",
                "paddingTop": "22px"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "Total: 6 hours",
                    "color": "#b7b7b7",
                    "size": "xs"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "text",
                        "text": "09:00",
                        "size": "sm",
                        "gravity": "center",
                        "align": "end"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "filler"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [],
                            "cornerRadius": "30px",
                            "height": "12px",
                            "width": "12px",
                            "borderColor": "#EF454D",
                            "borderWidth": "2px"
                        },
                        {
                            "type": "filler"
                        }
                        ],
                        "flex": 0
                    },
                    {
                        "type": "text",
                        "text": "Start",
                        "gravity": "center",
                        "flex": 4,
                        "size": "sm"
                    }
                    ],
                    "spacing": "lg",
                    "cornerRadius": "30px",
                    "margin": "xl"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "text",
                            "text": "3hr",
                            "gravity": "center",
                            "size": "xs",
                            "color": "#8c8c8c",
                            "align": "end"
                        }
                        ],
                        "flex": 1
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "filler"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [],
                                "width": "2px",
                                "backgroundColor": "#6486E3"
                            },
                            {
                                "type": "filler"
                            }
                            ],
                            "flex": 1
                        }
                        ],
                        "width": "12px"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "Recap LINE Bot Concepts",
                            "gravity": "center",
                            "size": "xs",
                            "color": "#8c8c8c"
                        },
                        {
                            "type": "text",
                            "text": "Flex Message Simulator",
                            "gravity": "center",
                            "size": "xs",
                            "color": "#8c8c8c"
                        }
                        ],
                        "flex": 4,
                        "justifyContent": "center"
                    }
                    ],
                    "spacing": "lg",
                    "height": "72px"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "text",
                            "text": "12:00",
                            "gravity": "center",
                            "size": "sm",
                            "align": "end"
                        }
                        ],
                        "flex": 1
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "filler"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [],
                            "cornerRadius": "30px",
                            "width": "12px",
                            "height": "12px",
                            "borderWidth": "2px",
                            "borderColor": "#6486E3"
                        },
                        {
                            "type": "filler"
                        }
                        ],
                        "flex": 0
                    },
                    {
                        "type": "text",
                        "text": "Break",
                        "gravity": "center",
                        "flex": 4,
                        "size": "sm"
                    }
                    ],
                    "spacing": "lg",
                    "cornerRadius": "30px"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "text",
                            "text": "1hr",
                            "gravity": "center",
                            "size": "xs",
                            "color": "#8c8c8c",
                            "align": "end"
                        }
                        ],
                        "flex": 1
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "filler"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [],
                                "width": "2px",
                                "backgroundColor": "#B7B7B7"
                            },
                            {
                                "type": "filler"
                            }
                            ],
                            "flex": 1
                        }
                        ],
                        "width": "12px"
                    },
                    {
                        "type": "text",
                        "text": "Lunch",
                        "gravity": "center",
                        "flex": 4,
                        "size": "xs",
                        "color": "#8c8c8c"
                    }
                    ],
                    "spacing": "lg",
                    "height": "24px"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "text",
                        "text": "13:00",
                        "gravity": "center",
                        "size": "sm",
                        "align": "end"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "filler"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [],
                            "cornerRadius": "30px",
                            "width": "12px",
                            "height": "12px",
                            "borderColor": "#EF454D",
                            "borderWidth": "2px"
                        },
                        {
                            "type": "filler"
                        }
                        ],
                        "flex": 0
                    },
                    {
                        "type": "text",
                        "text": "Continue",
                        "gravity": "center",
                        "flex": 4,
                        "size": "sm"
                    }
                    ],
                    "spacing": "lg",
                    "cornerRadius": "30px"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "text",
                            "text": "3hr",
                            "gravity": "center",
                            "size": "xs",
                            "color": "#8c8c8c",
                            "align": "end"
                        }
                        ],
                        "flex": 1
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "filler"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [],
                                "width": "2px",
                                "backgroundColor": "#6486E3"
                            },
                            {
                                "type": "filler"
                            }
                            ],
                            "flex": 1
                        }
                        ],
                        "width": "12px"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "Project Creation Ⅰ",
                            "gravity": "center",
                            "size": "xs",
                            "color": "#8c8c8c"
                        }
                        ],
                        "flex": 4,
                        "justifyContent": "center"
                    }
                    ],
                    "spacing": "lg",
                    "height": "72px"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "text",
                        "text": "16:00",
                        "gravity": "center",
                        "size": "sm",
                        "align": "end"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "filler"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [],
                            "cornerRadius": "30px",
                            "width": "12px",
                            "height": "12px",
                            "borderColor": "#6486E3",
                            "borderWidth": "2px"
                        },
                        {
                            "type": "filler"
                        }
                        ],
                        "flex": 0
                    },
                    {
                        "type": "text",
                        "text": "Happy Ending",
                        "gravity": "center",
                        "flex": 4,
                        "size": "sm"
                    }
                    ],
                    "spacing": "lg",
                    "cornerRadius": "30px"
                }
                ]
            }
            },
            {
            "type": "bubble",
            "size": "mega",
            "header": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "Jan. 5, 2025",
                        "color": "#ffffff",
                        "size": "sm"
                    }
                    ],
                    "position": "absolute",
                    "offsetStart": "200px",
                    "offsetTop": "15px"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "FROM",
                        "color": "#ffffff66",
                        "size": "sm"
                    },
                    {
                        "type": "text",
                        "text": "Anywhere",
                        "color": "#ffffff",
                        "size": "xl",
                        "flex": 4,
                        "weight": "bold"
                    }
                    ]
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "TO",
                        "color": "#ffffff66",
                        "size": "sm"
                    },
                    {
                        "type": "text",
                        "text": "NTUE F401b",
                        "color": "#ffffff",
                        "size": "xl",
                        "flex": 4,
                        "weight": "bold"
                    }
                    ]
                }
                ],
                "paddingAll": "20px",
                "backgroundColor": "#004B97",
                "spacing": "md",
                "height": "154px",
                "paddingTop": "22px"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "Total: 6 hours",
                    "color": "#b7b7b7",
                    "size": "xs"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "text",
                        "text": "09:00",
                        "size": "sm",
                        "gravity": "center",
                        "align": "end"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "filler"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [],
                            "cornerRadius": "30px",
                            "height": "12px",
                            "width": "12px",
                            "borderColor": "#EF454D",
                            "borderWidth": "2px"
                        },
                        {
                            "type": "filler"
                        }
                        ],
                        "flex": 0
                    },
                    {
                        "type": "text",
                        "text": "Start",
                        "gravity": "center",
                        "flex": 4,
                        "size": "sm"
                    }
                    ],
                    "spacing": "lg",
                    "cornerRadius": "30px",
                    "margin": "xl"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "text",
                            "text": "3hr",
                            "gravity": "center",
                            "size": "xs",
                            "color": "#8c8c8c",
                            "align": "end"
                        }
                        ],
                        "flex": 1
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "filler"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [],
                                "width": "2px",
                                "backgroundColor": "#6486E3"
                            },
                            {
                                "type": "filler"
                            }
                            ],
                            "flex": 1
                        }
                        ],
                        "width": "12px"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "Azure AI LINE Bot",
                            "gravity": "center",
                            "size": "xs",
                            "color": "#8c8c8c"
                        }
                        ],
                        "flex": 4,
                        "justifyContent": "center"
                    }
                    ],
                    "spacing": "lg",
                    "height": "72px"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "text",
                            "text": "12:00",
                            "gravity": "center",
                            "size": "sm",
                            "align": "end"
                        }
                        ],
                        "flex": 1
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "filler"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [],
                            "cornerRadius": "30px",
                            "width": "12px",
                            "height": "12px",
                            "borderWidth": "2px",
                            "borderColor": "#6486E3"
                        },
                        {
                            "type": "filler"
                        }
                        ],
                        "flex": 0
                    },
                    {
                        "type": "text",
                        "text": "Break",
                        "gravity": "center",
                        "flex": 4,
                        "size": "sm"
                    }
                    ],
                    "spacing": "lg",
                    "cornerRadius": "30px"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "text",
                            "text": "1hr",
                            "gravity": "center",
                            "size": "xs",
                            "color": "#8c8c8c",
                            "align": "end"
                        }
                        ],
                        "flex": 1
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "filler"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [],
                                "width": "2px",
                                "backgroundColor": "#B7B7B7"
                            },
                            {
                                "type": "filler"
                            }
                            ],
                            "flex": 1
                        }
                        ],
                        "width": "12px"
                    },
                    {
                        "type": "text",
                        "text": "Lunch",
                        "gravity": "center",
                        "flex": 4,
                        "size": "xs",
                        "color": "#8c8c8c"
                    }
                    ],
                    "spacing": "lg",
                    "height": "24px"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "text",
                        "text": "13:00",
                        "gravity": "center",
                        "size": "sm",
                        "align": "end"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "filler"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [],
                            "cornerRadius": "30px",
                            "width": "12px",
                            "height": "12px",
                            "borderColor": "#EF454D",
                            "borderWidth": "2px"
                        },
                        {
                            "type": "filler"
                        }
                        ],
                        "flex": 0
                    },
                    {
                        "type": "text",
                        "text": "Continue",
                        "gravity": "center",
                        "flex": 4,
                        "size": "sm"
                    }
                    ],
                    "spacing": "lg",
                    "cornerRadius": "30px"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "text",
                            "text": "3hr",
                            "gravity": "center",
                            "size": "xs",
                            "color": "#8c8c8c",
                            "align": "end"
                        }
                        ],
                        "flex": 1
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "filler"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [],
                                "width": "2px",
                                "backgroundColor": "#6486E3"
                            },
                            {
                                "type": "filler"
                            }
                            ],
                            "flex": 1
                        }
                        ],
                        "width": "12px"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "Project Creation Ⅱ",
                            "gravity": "center",
                            "size": "xs",
                            "color": "#8c8c8c"
                        },
                        {
                            "type": "text",
                            "text": "Project Sharing",
                            "gravity": "center",
                            "size": "xs",
                            "color": "#8c8c8c"
                        }
                        ],
                        "flex": 4,
                        "justifyContent": "center"
                    }
                    ],
                    "spacing": "lg",
                    "height": "72px"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "text",
                        "text": "16:00",
                        "gravity": "center",
                        "size": "sm",
                        "align": "end"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "filler"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [],
                            "cornerRadius": "30px",
                            "width": "12px",
                            "height": "12px",
                            "borderColor": "#6486E3",
                            "borderWidth": "2px"
                        },
                        {
                            "type": "filler"
                        }
                        ],
                        "flex": 0
                    },
                    {
                        "type": "text",
                        "text": "Happy Ending",
                        "gravity": "center",
                        "flex": 4,
                        "size": "sm"
                    }
                    ],
                    "spacing": "lg",
                    "cornerRadius": "30px"
                }
                ]
            }
            }
        ]
    }"""