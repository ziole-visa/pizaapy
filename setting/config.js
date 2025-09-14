const fs = require('fs')
// shadow x Ziole new era
global.owner = "6281250555198" // ganti aja 
global.footer = "shadow x" 
global.namabot = "shadow x" 
global.status = true 
global.namaowner = "shadow x"
global.idsaluran = "-"
global.imgmenu = "https://files.catbox.moe/0whvll.png"

// power by zeno os
// bisa ddos? gak peduli wak
// mau ganti ? ganti aja paling nanti eror wkwkwkwkwkwk
// shadow x
global.dana = `081250555198`
global.gopay = `081250555198`
global.ovo = "-"
global.shope = "-"
global.bank = "-"
global.namastore = "`none?????`"
global.lol = "";
global.msg = {
    owner: "You Are Not Owner",
    premium: "You Are Not Premium Member",
    admin: "You Are Not Admin",
    adminbot: "Me Not Admin",
    priv: "khusus pribadi",
    bot: "khusus nomer bot"
}
// sesuain aja wok
global.autoTyping = false 

global.panik = "wkwkwkwk berani ganti berarti kalau eror janagn salahin gw"
global.punyazioledanzeyykalauadayangranamesendnonya = `zensdi_8292326764023472345498327978797324987hi3d9` //token zeno
global.zenidtoken = 'zenid_-wefiu43H5IH5IJHG5UHBUB5I6BIB2UBU56GU46GBHJ34B5U34B5U3B5U3B5UJ345UY34B5UB34UY5BI35BUQC=-NTUY2GBU56G2564568UCTGBUW4GTCUY2GBUTYCGUYGUYGCBUEGBFCUYEGUYCFGSIUFCGUIYSERGFCIUYWEGFUYICSEUIF37TRG7Q3GT8C3G8IYFA'

// lu gw ?

let file = require.resolve(__filename)
require('fs').watchFile(file, () => {
  require('fs').unwatchFile(file)
  console.log('\x1b[0;32m'+__filename+' \x1b[1;32mupdated!\x1b[0m')
  delete require.cache[file]
  require(file)
})
