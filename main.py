'''
Author: thund1r thuncoder@foxmail.com
Date: 2022-08-27 14:47:01
LastEditTime: 2022-09-17 11:13:46
Description: 主函数

Copyright (c) 2022 by thund1r thuncoder@foxmail.com, All Rights Reserved. 
'''
# -*- coding: utf8 -*-
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
import uvicorn
import os


app = FastAPI()
index_html = """
<!DOCTYPE html>
<html lang="zh-CN">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon"
        href="https://fastly.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.1.1/svgs/regular/calendar-check.svg">
    <title>Diary</title>
</head>

<body>
    <section>
        <div class="container">
            Diary
        </div>
    </section>
</body>
<style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    body {
        background: linear-gradient(to bottom right, #0184cf, #77A1D3, #a0eacf);
    }

    .container {
        position: relative;
        display: flex;
        justify-content: center;
        align-items: center;
        color: white;
        font-size: 100px;
    }

    section {
        position: relative;
        overflow: hidden;
        display: flex;
        justify-content: center;
        min-height: 100vh;
    }
</style>

</html>
"""

show_html = """
<!DOCTYPE html>
<html lang="zh-CN">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon"
        href="https://fastly.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.1.1/svgs/regular/calendar-check.svg">
    <title>Diary</title>
</head>

<body>
    <section>
        <div class="container">
            <div class="pic">
                <img src='<&p&>'>
                </img>
            </div>
            <h2 class="title">
                <&t&>
            </h2>
            <h3 class="content">
                <&c&>
            </h3>
        </div>
        <div id="footer">- © 2022 Thund1R -</div>
    </section>
</body>
<style>
    /* 下面这三行切勿有任何变动 */
    .pic{display:none}
    .title{display:none}
    .content{display:none}

    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    .container {
        width: 50%;
        padding-bottom: 60px;
    }

    @media screen and (max-width: 1200px) {
        .container {
            width: 90%;
        }
    }

    body {
        background: linear-gradient(to bottom right, #0184cf, #77A1D3, #a0eacf);
    }


    .pic {
        margin: 16px 0;
        padding: 12px;
        background-color: white;
        border-radius: 8px;
        text-align: center;
        font-size: 0;
    }

    .title {
        margin: 16px 0 6px;
        color: #fff;
    }

    img {
        max-width: 100%;
        max-height: 100%;
    }

    .content {
        color: white;
    }

    section {
        position: relative;
        overflow: hidden;
        display: flex;
        justify-content: center;
        min-height: 100vh;
    }

    #footer {
        position: absolute;
        bottom: 0;
        text-align: center;
        line-height: 60px;
        color: white;
        font-weight: bold;
        width: 100%;
        height: 60px;
        clear: both;
    }
</style>

</html>
"""


@app.get('/')
async def main():
    return HTMLResponse(index_html)


@app.get("/show")
async def show(p=Query(None), t=Query(None), c=Query(None)):
    html = show_html
    if p:
        html = html.replace(".pic{display:none}", "").replace("<&p&>", p)
    if t:
        t = t.replace("\\n", "<br/>")
        html = html.replace(".title{display:none}", "").replace("<&t&>", t)
    if c:
        c = c.replace("\\n", "<br/>")
        html = html.replace(".content{display:none}", "").replace("<&c&>", c)
    return HTMLResponse(html)

if __name__ == '__main__':
    uvicorn.run(app='main:app', host="127.0.0.1",
                port=10086, reload=True, debug=True)
