<!--
 * @Author: cn_lion
 * @Date: 2022-06-13 14:35:53
 * @LastEditTime: 2022-06-13 17:58:11
 * @description: description your project
 * @FilePath: \crawler\qianfeng.md
-->
B站爬取实例测试


1、爬取up主千锋教育下投稿视频的相关信息
    整理获取到的数据
    av : av号
    bv : bv号
    title : 视频标题
    comment : 评论数
    plays : 播放数
    length : 时长
    time : 创建时间
    description : 视频简介
    pic : 视频封面
    p : 分p情况
        cid : cid号码
        title : 分p标题
        length : 分p时长


2、爬取某一视频下的评论或弹幕




获取视频信息：分p，cid，
https://api.bilibili.com/x/player/pagelist?bvid=BV1qb4y1Y722&jsonp=jsonp

获取弹幕信息，需cid，有数量限制
https://comment.bilibili.com/423412540.xml

获取视频评论
https://api.bilibili.com/x/v2/reply/main?mode=2&next=46&oid=633582932&plat=1&type=1

获取博主播放量获赞数，需要登陆的cookies 
https://api.bilibili.com/x/space/upstat?mid=146668655&jsonp=jsonp

获取用户信息
https://api.bilibili.com/x/space/acc/info?mid=600000000&jsonp=jsonp

获取博主粉丝数和关注数
https://api.bilibili.com/x/relation/stat?vmid=146668655&jsonp=jsonp