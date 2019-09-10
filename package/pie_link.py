"""发送邮件生成的饼型统计图"""

HTML = '''<!DOCTYPE html>
<html style="height: %s">
   <head>
       <meta charset="utf-8">
   </head>
   <body style="height: %s; margin: 0">
       <div id="container" style="height: %s"></div>
       <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts/echarts.min.js"></script>
       <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts-gl/echarts-gl.min.js"></script>
       <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts-stat/ecStat.min.js"></script>
       <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts/extension/dataTool.min.js"></script>
       <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts/map/js/china.js"></script>
       <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts/map/js/world.js"></script>
       <!--<script type="text/javascript" src="https://api.map.baidu.com/api?v=2.0&ak=xfhhaTThl11qYVrqLZii6w8qE5ggnhrY&__ec_v__=20190126"></script>-->
       <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts/extension/bmap.min.js"></script>
       <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/simplex.js"></script>
       <script type="text/javascript">
var dom = document.getElementById("container");
var myChart = echarts.init(dom);
// var app = {};
option = null;

setTimeout(function () {
    option = {
        legend: {
            //orient: 'vertical',
            center: '30px',
            bottom: 520,
        },
        title: {
        text: '%s',
        subtext: '%s',
        bottom: 910,
        left: 'center',
    },
        tooltip: {
            trigger: 'axis',
            showContent: true,
        },
        color : ['#EA0000', '#B87070', '#8E8E8E', '#006000', '#FFA500', '#00BFFF'], // 饼型图背景颜色重写
        dataset: {
            source: [
                ['product', '错误数', '失败数', '跳过数', '成功数', '预期失败', '意外成功'],
                ['错误数', '%s'],
                ['失败数', '%s'],
                ['跳过数', '%s'],
                ['成功数', '%s'],
                ['预期失败数', '%s'],
                ['意外成功数', '%s'],
            ]
        },
        xAxis: [
            {
                type: 'category',
                axisTick: {
                    alignWithLabel: true
                }
            }
        ],
        yAxis: {gridIndex: 0},
        grid: {top: '%s'},
        series: [
            // {type: 'line', smooth: true, seriesLayoutBy: 'column'},
            // {type: 'line', smooth: true, seriesLayoutBy: 'column'},
            // {type: 'line', smooth: true, seriesLayoutBy: 'column'},
            {type: 'line', smooth: false, seriesLayoutBy: 'column'},
            {
                type: 'pie',
                id: 'pie',
                radius: '%s',
                center: ['%s', '%s'],
                label: {
                    formatter: '%s'
                },
                encode: {
                    itemName: 'product',
                    value: '错误数',
                    tooltip: '成功数'
                }
            },
        ]
    };

    myChart.setOption(option);

});
if (option && typeof option === "object") {
    myChart.setOption(option, true);
}
       </script>
   </body>
</html>

'''