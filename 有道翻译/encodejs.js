var r, i, o, a, s = function (e, t) {
    return new s.fn.init(e, t, r)
}

function a(e, t) {
    var n = e("./jquery-1.7");
    e("./utils");
    e("./md5");
    var r = function (e) {
        var t = n.md5(navigator.appVersion)
            , r = "" + (new Date).getTime()
            , i = r + parseInt(10 * Math.random(), 10);
        return {
            ts: r,
            bv: t,
            salt: i,
            sign: n.md5("fanyideskweb" + e + i + "n%A-rKaT5fb[Gy?;N5@Tj")
        }
    }
}


console(a("define", "75551116684a442e8625ebfc9e5af1ba"))
