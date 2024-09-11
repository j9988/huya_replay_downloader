import requests
import os
import subprocess
def download(url,name, firsturl):
    urls=firsturl+url
    r = requests.get(urls)
    name = name+'.ts'
    with open(name,'wb') as f:
        f.write(r.content)

def get_mp4_ts (ts_path, mp4_path):
    try:
        print("--将合并ts文件转换为mp4格式--")
        subprocess.run(['ffmpeg', '-i', ts_path, mp4_path])
    except OSError as os:
        print("OSError: ", os, "\n")
        print("转换失败")
    except ValueError as ve:
        print("ValueError: Couldn't call FFMPEG with these parameters: ", ve, "\n")
        print("转换失败")
    else:
        print('转换完毕')

if __name__ == '__main__':
    i = 1
    j = 1
    filename = input('合并视频名称：')
    f = open("%s.ts"%filename, "w")
    f.close()
    firsturl = input('虎牙m3u8地址: ')
    input_path = input('m3u8文档地址: ')
    m3u8_path = input_path.replace('\\', "/")
    m3u8 = open(m3u8_path, 'r')
    lines=m3u8.readlines()

    for line in lines:
        if len(line) > 150:
            j = j + 1
    print("合并ts数量: ", j)

    for line in lines:
        if len(line)>150:
            download(line,str(i), firsturl)
            print("合并进度: ", i, "/", j)
            os.system('type %s.ts >> %s.ts'%(str(i), filename))
            i=i+1
    print('下载并合并完成')

    i = i-1
    print('删除多余文件中')
    for line in lines:
        if len(line)>150:
            os.remove(str(i)+'.ts')
            print("删除进度: ", j-i, "/", j)
            i=i-1
    print('下载完毕')

    input_path = input('ts地址: ')
    ts_path = input_path.replace('\\', "/")
    input_path = input('MP4存储地址: ')
    mp4_path = input_path.replace('\\', "/")
    get_mp4_ts(ts_path, mp4_path)
